from django.conf.urls import patterns, url
from django.contrib.auth.views import login, logout
from tutorhub import views

urlpatterns = patterns('',
    url(r'^sessions/$', views.SessionList.as_view()),
    url(r'^sessionform/$', views.AddSession.as_view()),
    url(r'^register/$', views.register),
    url(r'^login/$', login),
    url(r'^logout/$', logout, {'next_page': '/'}),
)


