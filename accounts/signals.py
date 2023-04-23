from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User 
from student.models import Student

@receiver(post_save,sender=User)
def post_save_create_profile_receiver(sender,instance,created,**kwargs):
    print(created)
    if created:
        if instance.role == 1:
            Student.objects.create(user=instance)
            print("Student object created")
        elif instance.role == 2:
            pass
            # create teacher object
        else:
            pass
    else:
        try:
            if instance.role == 1:
                student = Student.objects.get(user=instance)
                student.save()
                print("Student Object Updated")
            elif instance.role == 2:
                pass
            # save teacher object
        except:
            # create the user profile if it does not exist
            if instance.role == 1 :
                student = Student.objects.create(user=instance)
                print("Student object didnt exist but I created it")
            elif instance.role == 2:
                pass
        print('user is updated')