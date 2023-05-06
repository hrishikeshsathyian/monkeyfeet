from django.urls import path
from . import views
urlpatterns = [
        # LANDING PAGE
        path('homepage',views.homepage,name='student_homepage'),
        # ABOUT PAGE
        path('about',views.about,name='about'),
        # ASSIGNMENTS
        path('assignments',views.assignments,name='assignments'),
        path('delete_assignment/<uuid:unique_id>',views.delete_assignment,name='delete_assignment'),
        # PROFILE SETTINGS
        path('profile_settings',views.profile_settings,name='profile_settings')
    ]