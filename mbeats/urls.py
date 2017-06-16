__author__ = 'techno'
from django.conf.urls import url
from . import views

app_name = 'mbeats'

urlpatterns = [
    url(r'^$', views.base, name='base'),
    url(r'^index', views.index, name='index'),
    url(r'^login', views.login, name='login'),
    url(r'^register', views.register, name='register'),
    url(r'^logout', views.logout, name='logout'),
    url(r'^about', views.about, name='about'),
    url(r'^contact', views.contact, name='contact'),
    url(r'^base_user', views.base_user, name='base_user'),

]
