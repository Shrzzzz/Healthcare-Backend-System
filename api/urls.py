from django.urls import path
from .views import (
    RegisterView, LoginView,
    PatientCreateView, PatientListView, PatientDetailView,
    DoctorCreateView, DoctorListView, DoctorDetailView,
    PatientDoctorMappingView, PatientDoctorMappingListView, PatientDoctorMappingDetailView
)
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    # Authentication APIs
    path('auth/register/', RegisterView.as_view()),
    path('auth/login/', LoginView.as_view()),

    # Patient Management APIs
    path('patients/', PatientCreateView.as_view()),              # POST
    path('patients/list/', PatientListView.as_view()),           # GET
    path('patients/<int:pk>/', PatientDetailView.as_view()),     # GET, PUT, DELETE

    # Doctor Management APIs
    path('doctors/', DoctorCreateView.as_view()),                # POST
    path('doctors/list/', DoctorListView.as_view()),             # GET
    path('doctors/<int:pk>/', DoctorDetailView.as_view()),       # GET, PUT, DELETE

    # Patient-Doctor Mapping APIs
    path('mappings/', PatientDoctorMappingView.as_view()),              # POST
    path('mappings/list/', PatientDoctorMappingListView.as_view()),     # GET
    path('mappings/<int:pk>/', PatientDoctorMappingDetailView.as_view()), # GET, DELETE

    path('login/', obtain_auth_token, name='api_token_auth'),
]
