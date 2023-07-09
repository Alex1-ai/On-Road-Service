from django.urls import path

from roadservice import views


urlpatterns = [
    path('', views.home, name='home'),
    path('service', views.service, name='service'),
    path('createAccount', views.createAccount, name='createAccount'),
    path('login', views.login, name='login'),
    path('contact', views.contact, name='contact'),
    path('serviceForm', views.serviceForm, name='serviceForm'),
    path('logout', views.logout, name='logout')

]
