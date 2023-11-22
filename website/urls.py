from django.urls import path
from . import views


urlpatterns = [
    # General URLs
    path('', views.home, name='home'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),

    # Patient Management URLs

    path('patient_management/', views.see_patient_management, name='patient_management'),

    # Patient URLs
    path('patient_management/patient_table/', views.see_patient_table, name='patient_table'),
    path('patient_management/patient<int:pk>', views.patient_record, name='patient'),
    path('patient_management/delete_patient<int:pk>', views.delete_patient, name='delete_patient'),
    path('patient_management/add_patient/', views.add_patient, name='add_patient'),
    path('patient_management/update_patient/<int:pk>', views.update_patient, name='update_patient'),
    
    # Request URLs
    path('patient_management/request_table/', views.see_request_table, name='request_table'),
    path('patient_management/request<int:pk>', views.request_record, name='request'),
    path('patient_management/delete_request<int:pk>', views.delete_request, name='delete_request'),
    path('patient_management/add_request/', views.add_request, name='add_request'),
    path('patient_management/update_request/<int:pk>', views.update_request, name='update_request'),
    
    # Distinct Function URLs for Patient Management

    path('patient_management/search_appointments/', views.search_appointments, name='search_appointments'),
    path('patient_management/view_medical_history/<int:pk>/', views.view_medical_history, name='view_medical_history'),

    # In_Patient Management URLs
    path('in_patient_management/', views.see_in_patient_management, name='in_patient_management'),

    # Bed URLs
    path('in_patient_management/bed_table/', views.see_bed_table, name='bed_table'),
    path('in_patient_management/bed<int:pk>', views.bed_record, name='bed'),
    path('in_patient_management/delete_bed<int:pk>', views.delete_bed, name='delete_bed'),
    path('in_patient_management/add_bed/', views.add_bed, name='add_bed'),
    path('in_patient_management/update_bed/<int:pk>', views.update_bed, name='update_bed'),


    # Room URLs
    path('in_patient_management/room_table/', views.see_room_table, name='room_table'),
    path('in_patient_management/room<int:pk>', views.room_record, name='room'),
    path('in_patient_management/delete_room<int:pk>', views.delete_room, name='delete_room'),
    path('in_patient_management/add_room/', views.add_room, name='add_room'),
    path('in_patient_management/update_room/<int:pk>', views.update_room, name='update_room'),

    # InPatient URLs
    path('in_patient_management/inpatient_table/', views.see_inpatient_table, name='inpatient_table'),
    path('in_patient_management/inpatient<int:pk>', views.inpatient_record, name='inpatient'),
    path('in_patient_management/delete_inpatient<int:pk>', views.delete_inpatient, name='delete_inpatient'),
    path('in_patient_management/add_inpatient/', views.add_inpatient, name='add_inpatient'),
    path('in_patient_management/update_inpatient/<int:pk>', views.update_inpatient, name='update_inpatient'),

    # Medical Staff Management URLs
    
        # Patient Management URLs

    path('medical_staff_management/', views.see_medical_staff_management, name='medical_staff_management'),

    
    # Doctor URLs
    path('medical_staff_management/doctor_table/', views.see_doctor_table, name='doctor_table'),
    path('medical_staff_management/doctor<int:pk>', views.doctor_record, name='doctor'),
    path('medical_staff_management/delete_doctor<int:pk>', views.delete_doctor, name='delete_doctor'),
    path('medical_staff_management/add_doctor/', views.add_doctor, name='add_doctor'),
    path('medical_staff_management/update_doctor/<int:pk>', views.update_doctor, name='update_doctor'),

    # Appointment URLs
    path('medical_staff_management/appointment_table/', views.see_appointment_table, name='appointment_table'),
    path('medical_staff_management/appointment<int:pk>', views.appointment_record, name='appointment'),
    path('medical_staff_management/delete_appointment<int:pk>', views.delete_appointment, name='delete_appointment'),
    path('medical_staff_management/add_appointment/', views.add_appointment, name='add_appointment'),
    path('medical_staff_management/update_appointment/<int:pk>', views.update_appointment, name='update_appointment'),
    




]