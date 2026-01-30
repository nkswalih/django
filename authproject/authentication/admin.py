from django.contrib import admin
from .models import Student, Doctor, Patient

admin.site.register(Student)
admin.site.register(Doctor)
admin.site.register(Patient)