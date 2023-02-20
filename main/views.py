from django.shortcuts import render
from django.views.generic import ListView

from .models import Information


# Create your views here.


class GeneralPage(ListView):
    model = Information
    template_name = 'index.html'
