from django.db import models
from student.models import Student,Subject,TutorLevel
import uuid
# Create your models here

class Assignment(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE)
    hourly_rate = models.DecimalField(max_digits=2,decimal_places=0,blank=False,null=True)
    preferred_gender = models.CharField(max_length=50,choices=Student.GENDER_PREFERENCE_CHOICES,blank=False,null=True)
    address = models.CharField(max_length=250,blank=False,null=True)
    preferred_tutor_level = models.ManyToManyField(TutorLevel,blank=False)
    additional_information = models.TextField()
    unique_id = models.UUIDField(unique=True,default=uuid.uuid4,editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.unique_id
    # tutor = models.ManytoManyKey
