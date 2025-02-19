# Create your views here.
from django.shortcuts import render, redirect
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


class AdminPage(TemplateView):
    template_name = 'admin_page.html'


class UserLoginView(LoginView):
    template_name = 'registration/login.html'
    redirect_authenticated_user = True
    success_url = reverse_lazy('main_page')

    def get_success_url(self):
        return self.success_url


class UserRegisterView(FormView):
    template_name = 'registration/user_registration.html'
    form_class = NewUserForm
    success_url = reverse_lazy('main_page')

    def form_valid(self, form):
        user = form.save() # zapisanie użytkownika, FormView nie robi tego automatycznie
        login(self.request, user) # zalogowanie użytkownika
        return super().form_valid(form)


class UserLogoutView(LogoutView):
    redirect_authenticated_user = True
    success_url = 'main_page'


class CreateDoctorView(FormView):
    template_name = "doctor.html"
    form_class = CreateDoctor
    success_url = reverse_lazy('admin_page')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class CreateDoctorTypeView(FormView):
    template_name = "specialization.html"
    form_class = CreateDoctorType
    success_url = reverse_lazy('admin_page')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class AppointmentDatesView(FormView):
    template_name = "appointment_date.html"
    form_class = AppointmentDatesForm
    success_url = reverse_lazy('admin_page')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    

class DoctorTypeSelectView(FormView):
    template_name = 'doctor_visit.html'
    form_class = DoctorTypeSelect
    
    def form_valid(self, form):
        doctor_type = form.cleaned_data['doctor_type_select']
        return redirect('choose_doctor_name', pk=doctor_type.pk)


class DoctorNameSelectView(FormView):
    model = DoctorName
    form_class = DoctorNameSelect
    template_name = 'choose_doctor_name.html'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        specialization_pk = self.kwargs.get('pk')
        # filtrowanie po specjalizacji
        kwargs['initial'] = {
            'doctor_name_select': DoctorName.objects.filter(main_specialization__pk=specialization_pk)
        }
        return kwargs
    
    def form_valid(self, form):
        doctor_name_spec = form.cleaned_data['doctor_name_select']
        return redirect('choose_visit_date_time', pk=doctor_name_spec.pk)


class VisitDateSelectView(FormView):
    model = AppointmentDates
    form_class = VisitDateSelect
    template_name = 'choose_visit_date_time.html'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        date_time_pk = self.kwargs.get('pk')
        # filtrowanie po specjalizacji
        kwargs['initial'] = {
            'doctor_date_select': DoctorName.objects.filter(appointmentdates__pk=date_time_pk)
        }
        return kwargs
    