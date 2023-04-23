from django.urls import path
from . import views
urlpatterns = [
        #landing page for students 
        path('homepage',views.homepage,name='student_homepage')
    ]