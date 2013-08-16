from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.conf import settings
from tutorhub import views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', views.SessionList.as_view()),
    url(r'^who/$', TemplateView.as_view(template_name='who.html')),
    url(r'^students/$', TemplateView.as_view(template_name='students.html')),
    url(r'^teachers/$', TemplateView.as_view(template_name='teachers.html')),
    url(r'^write/$', TemplateView.as_view(template_name='write.html')),
    url(r'^visit/$', TemplateView.as_view(template_name='visit.html')),
    # Examples:
    # url(r'^$', 'tutorsite.views.home', name='home'),
    # url(r'^tutorsite/', include('tutorsite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    url(r'^tutorhub/', include('tutorhub.urls')),
)
