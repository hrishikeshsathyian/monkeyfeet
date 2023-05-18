from django.db import models
from student.models import Student,Subject,TutorLevel
from tutors.models import Tutor
import uuid
# Create your models here

class Assignment(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE)
    hourly_rate = models.DecimalField(max_digits=2,decimal_places=0,blank=False,null=True)
    preferred_gender = models.CharField(max_length=50,choices=Student.GENDER_PREFERENCE_CHOICES,blank=False,null=True)
    address = models.CharField(max_length=250,blank=False,null=True)
    preferred_tutor_level = models.ManyToManyField(TutorLevel,blank=False)
    additional_information = models.TextField(max_length = 500, blank=True,null=True)
    unique_id = models.UUIDField(unique=True,default=uuid.uuid4,editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    tutor = models.ManyToManyField(Tutor,blank=True,related_name='applied_assignments')
    
    # tutor = models.ManytoManyKey
