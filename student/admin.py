from django.contrib import admin
from .models import Student, Subject, TutorLevel
# Register your models here.
admin.site.register(Student)
admin.site.register(Subject)
admin.site.register(TutorLevel)