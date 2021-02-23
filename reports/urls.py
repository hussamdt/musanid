from django.urls import path
from . import views

app_name = 'reports'
urlpatterns = [
    path('', views.index, name='index'),
    path('overall', views.index, name='overall'),
    path('all', views.reports, name='list'),
    path('<int:report_id>', views.single_report, name='single-report'),
    path('<int:report_id>/alert/<int:alert_id>', views.single_alert, name='single-alert'),
    path('generate_url', views.generate_url, name='generate'),
    path('url/<generated_url>', views.get_by_generated_url, name='by-generated-url'),
    path('url/<generated_url>/<int:alert_id>', views.by_generated_url_alert, name='by-generated-url-alert'),
    path('pdf/<generated_url>/<int:alert_id>', views.generate_pdf_for_generate_url, name='pdf-by-generated-url'),

    path('pdf/<int:alert_id>', views.generate_pdf, name='generate-pdf'),

    path('search', views.search, name='search'),
    path('statistic', views.get_statistic, name='search'),

    
    path('loader', views.data_loader, name='loader'),
    path('loader/start', views.start_loader, name='start-loader'),
    path('loader/stop', views.stop_loader, name='stop-loader'),
    
    #loading Dummy Data
    #path('load_data', views.load_data, name='load'),
]