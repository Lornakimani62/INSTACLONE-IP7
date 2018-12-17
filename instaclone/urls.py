from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$',views.index, name='index'),
    url(r'^signup$',views.signup, name='signup'),
    url(r'^ajax-sign-up$', views.ajaxsignup),
    url(r'^ajax-login$' , views.ajaxlogin)
]