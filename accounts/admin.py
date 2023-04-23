from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin
# Register your models here.
class CustomUserAdmin(UserAdmin):
    list_display = ('email','first_name','last_name','username','role','is_active') #limits what fields are shown in list display
    ordering = ('-date_joined',) # sorts users by date joined
    filter_horizontal = ()
    list_filter = ()
    fieldsets = () # the above 3 variables make password non-editable hash
admin.site.register(User,CustomUserAdmin)