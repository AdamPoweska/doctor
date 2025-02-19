from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import *

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class CreateDoctor(forms.ModelForm):
    class Meta:
        model = DoctorName
        fields = '__all__'
  

class CreateDoctorType(forms.ModelForm):
    class Meta:
        model = DoctorType
        fields = '__all__'


class AppointmentDatesForm(forms.ModelForm):
    class Meta:
        model = AppointmentDates
        fields = '__all__'


class DoctorTypeSelect(forms.Form):
    doctor_type_select = forms.ModelChoiceField(
        queryset=DoctorType.objects.all(),
        widget=forms.RadioSelect, # bez tego pojawi się lista rozwijana
        required=True
    )


class DoctorNameSelect(forms.Form):
    doctor_name_select = forms.ModelChoiceField(
        queryset=DoctorName.objects.all(),
        widget=forms.RadioSelect,
        required=True
    )

# NOWY WIDOK
class VisitDateSelect(forms.Form):
    doctor_date_select = forms.ModelChoiceField(
        queryset=AppointmentDates.objects.all(),
        widget=forms.RadioSelect,
        required=True
    )