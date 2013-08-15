from django.views import generic
from django import forms
from django.utils import timezone
from django.http import HttpResponseRedirect

from tutorhub import models

# Create your views here.

class SessionList(generic.ListView):
    model = models.Session

