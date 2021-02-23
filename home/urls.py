from django.urls import path
from . import views

app_name='home'
urlpatterns = [
    path('', views.home, name='home'),
    path('contact-us', views.contact, name='contact'),
    path('article/<int:article_id>', views.single_article, name ='article'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
]