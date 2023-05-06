from django.contrib import admin
from .models import Assignment
# Register your models here.

class CustomAssignmentAdmin(admin.ModelAdmin):
    readonly_fields = ['unique_id',]
    list_display = ('student','subject','address','hourly_rate') #limits what fields are shown in list display
    ordering = ('-created_at',) # sorts users by date joined

admin.site.register(Assignment,CustomAssignmentAdmin)