# Create your views here.
from django.views.generic import TemplateView, ListView
from django.shortcuts import render
from django.http import HttpResponse

class MainPage(TemplateView):
    template_name = 'main_page.html'


