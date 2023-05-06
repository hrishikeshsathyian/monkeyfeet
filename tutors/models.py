from django.db import models
from accounts.models import User
from student.models import Subject,TutorLevel,Student
# Create your models here.

class Tutor(models.Model):
    # model relationship
    user = models.OneToOneField(User,on_delete=models.CASCADE,blank=True,null=True)
    #personal information
    gender = models.CharField(max_length=50,choices=Student.GENDER_CHOICES,blank=False,null=True)
    profile_picture = models.ImageField(upload_to='users/profile_pictures',blank=True,null=True)
    address = models.CharField(max_length=250,blank=False,null=True)
    zip_code = models.CharField(max_length=6,blank=False,null=False)
    latitude = models.CharField(max_length=50,blank=True,null=False)
    longitude = models.CharField(max_length=50,blank=True,null=False)
    dob = models.DateField(blank=False,null=True)
    # credentials 
    subjects = models.ManyToManyField(Subject,blank=False)
    tutor_level = models.ForeignKey(TutorLevel,blank=False,on_delete=models.PROTECT,null=True)
    qualification_information = models.TextField(max_length=500,blank=True,null=True)
    certificate_credential = models.FileField(upload_to='users/tutors/certificate',blank=True,null=False)
    is_verified = models.BooleanField(default=False)
    # additional details 
    additional_information = models.TextField(max_length=500, blank=True,null=True)

    #misc 
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.user.email

