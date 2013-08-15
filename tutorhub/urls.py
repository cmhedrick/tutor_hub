from django.conf.urls import patterns, url
from tutorhub import views

urlpatterns = patterns('',
        url(r'^sessions/$', views.SessionList.as_view()),
        url(r'^sessionform/$', views.SessionForm.as_view()),
)


