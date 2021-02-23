from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.template.loader import get_template
from django.conf import settings
from django.utils import timezone
from .models import Report, Alert
import datetime
import uuid
from io import BytesIO

from xhtml2pdf import pisa

from .data_loader import loader

'''
    login required area
'''
@login_required()
def index(request):
    total_reports = Report.objects.all().count()
    total_alerts = Alert.objects.all().count()
    
    today = timezone.now().today()
    yesterday = today - datetime.timedelta(days=1)
    today_reports = Report.objects.filter(created_at__lte= today).filter(created_at__gte = yesterday)
    
    today_alerts = 0
    for report in today_reports:
        today_alerts += report.alert_set.all().count()
    
    last_week = today - datetime.timedelta(days=7)
    week_reports = Report.objects.filter(created_at__lte= today).filter(created_at__gte = last_week)
    
    week_alerts = 0
    for report in week_reports:
        week_alerts += report.alert_set.all().count()

    last_month = today - datetime.timedelta(days=30)
    month_reports = Report.objects.filter(created_at__lte= today).filter(created_at__gte = last_month)
    
    month_alerts = 0
    for report in month_reports:
        month_alerts += report.alert_set.all().count()

    context = { 'total_reports': total_reports,
                'today_reports': today_reports,
                'week_reports' : week_reports,
                'month_reports': month_reports,
                'total_alerts' : total_alerts,
                'today_alerts' : today_alerts,
                'week_alerts'  : week_alerts,
                'month_alerts' : month_alerts
            }
    
    return render(request, 'reports/index.html', {'context': context})

@staff_member_required
def data_loader(request):
    context = {
                'status'        :   loader.loader_status,
                'loaded_reports':   loader.get_loaded_reports(),
                'logs'          :   loader.get_logs(),
                'loader_status' :   loader.get_status(),
                'last_check'    :   loader.last_check,
                'next_check'    :   loader.next_check,
                }
    return render(request,'reports/loader.html', {'context': context})    

@staff_member_required
def start_loader(request):
    if loader.get_status() is False:
        loader.start_loader()
        return redirect('/reports/loader')
    else:
        return redirect('/reports/loader')

@staff_member_required
def stop_loader(request):
    loader.stop_loader()
    return redirect('/reports/loader')


@login_required()
def reports(request):
    reports = Report.objects.all()
    return render(request, 'reports/reports.html', {'reports': reports})
    
@login_required()
def single_report(request, report_id):
    report = get_object_or_404(Report, pk=report_id)
    print(report.get_full_url(request))
    return render(request, 'reports/alerts.html', {'report': report})


def get_by_generated_url(request, generated_url):
    report = get_object_or_404(Report, generated_url = generated_url)
    return render(request, 'reports/generated_url.html', {'report': report})

def by_generated_url_alert(request, generated_url, alert_id):
    report = get_object_or_404(Report, generated_url=generated_url)
    alert = report.alert_set.get(pk=alert_id)
    return render(request, 'reports/generated_url_alert.html', {'alert': alert})

def single_alert(request, report_id, alert_id):
    report = get_object_or_404(Report, pk=report_id)
    alert = report.alert_set.get(pk=alert_id)
    return render(request, 'reports/single_alert.html', {'alert': alert})
    
@staff_member_required
def generate_url(request):
    try:
        if request.method == 'GET':
            return HttpResponse('Direct Access Denied')
        
        report_id = request.POST['report_id']
        report = get_object_or_404(Report, pk=report_id)
        url_prefix = str(request.scheme) + '://' + str(request.get_host())
        url = str(uuid.uuid3(uuid.NAMESPACE_DNS, report.report_name))
        url = url.replace('-', '')
        report.generated_url = url
        report.save()
        url = '/reports/url/' + url
        generated_url = url_prefix + url
        return HttpResponse(generated_url)
    except Exception as e:
        return HttpResponse(e)


@login_required()
def search(request):
    query = request.GET['query']
    results = 'Sorry, we did not find any results for <strong>' + query + '</strong>'
    return render(request, 'reports/search_results.html', {'results': results})

@login_required()
def get_statistic(request):
    total   = Alert.objects.all().count()
    high    = Alert.objects.filter(priorty = 'High').count()
    medium  = Alert.objects.filter(priorty = 'Medium').count()
    low     = Alert.objects.filter(priorty = 'Low').count()
    
    # convert to percentage
    high    = (high * 100) / total
    medium  = (medium * 100) / total
    low     = (low * 100) / total
    
    response = {'high': int(high), 'medium': int(medium), 'low': int(low)}
    return JsonResponse(response)

# view to generate the pdf for given alert_id
@login_required()
def generate_pdf(request, alert_id):
    alert = get_object_or_404(Alert, pk=alert_id)
    date = timezone.now().date()
    pdf = render_pdf('reports/others/pdf_report.html', {'alert': alert, 'date': date})
    
    response = HttpResponse(pdf, content_type='application/pdf', )
    filename = f'Report_{alert.report}-Alert_{alert.alert_name}-{alert.time}.pdf'
    content  = f'inline; filename="{filename}"'

    download = request.GET.get('download')
    if download:
        if download == 'true':
            content  = f'attachment; filename="{filename}"'
    response['Content-Disposition'] = content
    return response

# view generates pdf for alerts got by generated url
def generate_pdf_for_generate_url(request, generated_url, alert_id):
    report = get_object_or_404(Report, generated_url=generated_url)
    alert  = report.alert_set.get(pk=alert_id)
    if alert:
        response = generate_pdf(request, alert_id)
        return response
    
    return redirect(request.get_host() + '/generated_url')



# function that generete pdf and render it to template given by view, return HttpResponse
def render_pdf(template_src, context_dict):
    template = get_template(template_src)
    html = template.render(context_dict)
    response = HttpResponse(content_type='application/pdf')

    #result = BytesIO()
    #pdf = pisa.pisaDocument(BytesIO(html.encode('ISO-8859-1')), result, link_callback=link_callback)
    pdf = pisa.CreatePDF(html, dest=response)
    if pdf.err:
        return HttpResponse('some thing went wronge - ' + html)
       
    return response#HttpResponse(result.getvalue(), content_type = 'application/pdf')
    



def link_callback(uri, rel):
    """
    Convert HTML URIs to absolute system paths so xhtml2pdf can access those
    resources
    """
    from django.contrib.staticfiles import finders
    result = finders.find(uri)
    if result:
            if not isinstance(result, (list, tuple)):
                    result = [result]
            result = list(os.path.realpath(path) for path in result)
            path=result[0]
    else:
            sUrl = settings.STATIC_URL        # Typically /static/
            sRoot = settings.STATIC_ROOT      # Typically /home/userX/project_static/
            mUrl = settings.MEDIA_URL         # Typically /media/
            mRoot = settings.MEDIA_ROOT       # Typically /home/userX/project_static/media/

            if uri.startswith(mUrl):
                    path = os.path.join(mRoot, uri.replace(mUrl, ""))
            elif uri.startswith(sUrl):
                    path = os.path.join(sRoot, uri.replace(sUrl, ""))
            else:
                    return uri

    # make sure that file exists
    if not os.path.isfile(path):
            raise Exception(
                    'media URI must start with %s or %s' % (sUrl, mUrl)
            )
    return path


        




