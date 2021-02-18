from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.utils import timezone
from .models import Report
import datetime
import uuid

'''
    login required area
'''
@login_required()
def index(request):
    
    total_reports = Report.objects.all().count()
    
    today = datetime.date.today()
    yesterday = today - datetime.timedelta(days=1)
    today_reports = Report.objects.filter(time__lte= today).filter(time__gte = yesterday)
    
    last_week = today - datetime.timedelta(days=7)
    week_reports = Report.objects.filter(time__lte= today).filter(time__gte = last_week)
    
    last_month = today - datetime.timedelta(days=30)
    month_reports = Report.objects.filter(time__lte= today).filter(time__gte = last_month)
    
    context = { 'total_reports': total_reports,
                'today_reports': today_reports,
                'week_reports' : week_reports,
                'month_reports': month_reports
            }
    
    return render(request, 'reports/index.html', {'context': context})
    
    
@login_required()
def reports(request):
    reports = Report.objects.all()
    return render(request, 'reports/reports.html', {'reports': reports})
    
@login_required()
def single_report(request, report_id):
    report = get_object_or_404(Report, pk=report_id)
    return render(request, 'reports/single_report.html', {'report': report})
    
@login_required()
def generate_url(request):
    try:
        if request.method == 'GET':
            return HttpResponse('Direct Access Denied')
        
        report_id = request.POST['report_id']
        report = get_object_or_404(Report, pk=report_id)
        url_prefix = str(request.scheme) + '://' + str(request.get_host())
        url = str(uuid.uuid3(uuid.NAMESPACE_DNS, report.alert_name))
        url = url.replace('-', '')
        generated_url = url_prefix + '/' + url
        report.generated_url = generated_url
        report.save()
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
    total   = Report.objects.all().count()
    high    = Report.objects.filter(priorty = 'High').count()
    medium  = Report.objects.filter(priorty = 'Medium').count()
    low     = Report.objects.filter(priorty = 'Low').count()
    
    # convert to percentage
    high    = (high * 100) / total
    medium  = (medium * 100) / total
    low     = (low * 100) / total
    
    response = {'high': int(high), 'medium': int(medium), 'low': int(low)}
    return JsonResponse(response)
    















def load_data(request):

    import pandas as pd
    import datetime

    data = pd.read_csv(settings.BASE_DIR / 'data.csv')
    summary = ''
    for row in range(data.shape[0]):
        
        report = Report()
        
        report.alert_type               =   data.iloc[row]['Alert_Type']
        report.alert_name               =   data.iloc[row]['Alert_Name']
        report.priorty                  =   data.iloc[row]['Priorty']
        report.malaware_family          =   data.iloc[row]['Malaware_family']
        report.http_hostname            =   data.iloc[row]['HTTP_Hostname']
        report.attack_reference         =   data.iloc[row]['Attack_reference']
        report.src_hostname             =   data.iloc[row]['Src_hostname']
        report.src_ip                   =   data.iloc[row]['Src_ip']
        report.dst_ip                   =   data.iloc[row]['Dst_ip']
        report.dst_country              =   data.iloc[row]['Dst_country']
        report.time                     =   datetime.datetime.now()                                                #data.iloc[row]['time']
        report.reference_url            =   data.iloc[row]['reference_URL']
        report.src_country              =   data.iloc[row]['src_Country']
        report.dst_hostname             =   data.iloc[row]['Dst_Hostname']
        report.recommendation           =   data.iloc[row]['Recommendation']
        report.description              =   data.iloc[row]['description']
        report.other_tls_subject        =   data.iloc[row]['Other_TLS_Subject']
        report.other_tls_fingerprint    =   data.iloc[row]['Other_TLS_Fingerprint']
        report.other_username           =   data.iloc[row]['Other_Username']
        report.other_source_nt_domain   =   data.iloc[row]['Other_SOURCE_NT_DOMAIN']
        report.other_destination_asset  =   data.iloc[row]['Other_DESTINATION_ASSET']
        report.other                    =   data.iloc[row]['OTHER']
        
        report.save()
        
        summary = summary+'<br>Saved record No: '+ str(row)
    
    return HttpResponse(summary)
        




