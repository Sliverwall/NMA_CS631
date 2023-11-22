from django.contrib import admin
from .models import Staff, Patient,Doctor,Nurse,MedicalHistory, Illness,Request,Bed,Room,InPatient,Appointment


admin.site.register(Staff)

admin.site.register(Patient)

admin.site.register(Doctor)

admin.site.register(Nurse)

admin.site.register(Illness)

admin.site.register(MedicalHistory)

admin.site.register(Request)

admin.site.register(Appointment)

admin.site.register(Bed)

admin.site.register(Room)

admin.site.register(InPatient)