from django.urls import path, include
from . import views
urlpatterns = [
    # login and registration
    path('login/',views.login,name='login'),
    path('register/tutor/',views.register_tutor, name='register_tutor'),
    path('register/student/',views.register_student,name='register_student'),
    path('logout/',views.logout,name='logout'),
    #email user account verification
    path('activate/<uidb64>/<token>',views.activate,name='activate'),
    
    ]
