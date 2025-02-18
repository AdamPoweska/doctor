# Create your views here.
from django.views.generic import TemplateView, ListView
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic.edit import FormView, CreateView
from django.contrib.auth import login

from . forms import *

class MainPage(TemplateView):
    template_name = 'main_page.html'

class DoctorVisit(TemplateView):
    template_name = 'doctor_visit.html'

class UserLoginView(LoginView):
    template_name = 'registration/login.html'
    redirect_authenticated_user = True
    success_url = reverse_lazy('doctor_visit')

    def get_success_url(self):
        return self.success_url


class UserRegisterView(FormView):
    template_name = 'registration/user_registration.html'
    form_class = NewUserForm
    success_url = reverse_lazy('doctor_visit')

    def form_valid(self, form):
        user = form.save() # zapisanie użytkownika, FormView nie robi tego automatycznie
        login(self.request, user) # zalogowanie użytkownika
        return super().form_valid(form)

class UserLogoutView(LogoutView):
    redirect_authenticated_user = True
    success_url = 'main_page'

    def get_success_url(self):
        return self.success_url
