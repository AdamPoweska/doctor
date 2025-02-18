from django.urls import path

from . import views

urlpatterns = [
    path("", views.MainPage.as_view(), name="main_page"),
    path('doctor_visit/', views.DoctorVisit.as_view(), name="doctor_visit"),
    path('admin_page/', views.AdminPage.as_view(), name='admin_page'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('user_registration/', views.UserRegisterView.as_view(), name='user_registration'),
    path('user_logout/', views.UserLogoutView.as_view(), name='user_logout'),
]