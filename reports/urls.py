from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('overall', views.index, name='overall'),
    path('all', views.reports, name='list'),
    path('single/<int:report_id>', views.single_report, name='single'),
    path('generate_url', views.generate_url, name='generate'),
    path('search', views.search, name='search'),
    path('statistic', views.get_statistic, name='search'),
    
    #loading Dummy Data
    path('load_data', views.load_data, name='load'),
]