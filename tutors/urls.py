from django.urls import path
from . import views
urlpatterns = [
        # LANDING PAGE
        path('homepage',views.homepage,name='tutor_homepage'),
        # PROFIEL SETTINGS 
        path('profile_settings',views.profile_settings,name='tutor_profile_settings'),
        # ASSIGNMENTS
        path('assignments',views.assignments,name='tutor_assignments'),
        path('apply_for_assignment/<uuid:unique_id>',views.apply_for_assignment,name='apply_for_assignment'),
       
    ]