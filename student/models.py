
from django.db import models
from accounts.models import User

# Create your models here.

class Subject(models.Model):
    GRADE_CHOICES = (
    ('Primary 1','Primary 1'),
    ('Primary 2','Primary 2'),
    ('Secondary 1','Secondary 1'),
    ('Secondary 2','Secondary 2')
    )
    grade = models.CharField(max_length=50,choices=GRADE_CHOICES)
    title = models.CharField(max_length=50)

    def __str__(self):
        x = self.grade + ' - ' + self.title 
        return x
    
class TutorLevel(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title
    

class Student(models.Model):
    GENDER_CHOICES = (
        ('MALE','MALE'),
        ('FEMALE','FEMALE'),
    )
    GENDER_PREFERENCE_CHOICES = (
        ('MALE','MALE'),
        ('FEMALE','FEMALE'),
        ('NO PREFERENCE','NO PREFERENCE')
    )
    TUTOR_LEVEL_CHOICES = (
        ('PART-TIME','PART-TIME'),
        ('FULL-TIME','FULL-TIME'),
    )

    # model relationships
    user = models.OneToOneField(User,on_delete=models.CASCADE,blank=True,null=True)
    # personal information
    gender = models.CharField(max_length=50,choices=GENDER_CHOICES,blank=False,null=True)
    profile_picture = models.ImageField(upload_to='users/profile_pictures',blank=True,null=True)
    address = models.CharField(max_length=250,blank=False,null=True)
    zip_code = models.CharField(max_length=6,blank=False,null=False)
    latitude = models.CharField(max_length=50,blank=True,null=False)
    longitude = models.CharField(max_length=50,blank=True,null=False)
    dob = models.DateField(blank=False,null=True)
    # preferences
    subjects = models.ManyToManyField(Subject,blank=False)
    preferred_gender = models.CharField(max_length=50,choices=GENDER_PREFERENCE_CHOICES,blank=False,null=True)
    preferred_tutor_level = models.ManyToManyField(TutorLevel,blank=False)
    
    #additional details 
    additional_information = models.TextField(max_length = 500, blank=True,null=True)
    # misc
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return self.user.email