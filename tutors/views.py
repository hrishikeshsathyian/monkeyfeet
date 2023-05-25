from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Tutor
from student.models import Student
from accounts.forms import TutorForm, UserForm
from django.contrib import messages
from assignments.models import Assignment
from django.db.models import Q
from accounts.utils import send_assignment_application_email
from django.contrib.gis.geos import GEOSGeometry
from django.contrib.gis.measure import D
from django.contrib.gis.db.models.functions import Distance
import sweetify
# Create your views here.
def homepage(request):
    tutor = Tutor.objects.get(user = request.user) # get logged in tutor
    # filter assignments to be shown to tutor 
    # filter assignments by gender
    assignments = Assignment.objects.filter(Q(preferred_gender=tutor.gender) | Q(preferred_gender='NO PREFERENCE'))
    # filter assignments by tutor level 
    assignments = assignments.filter(preferred_tutor_level__in = [tutor.tutor_level])
    # filters assignments by subject
    assignments = assignments.filter(subject__in = tutor.subjects.all())
    assignments = assignments.order_by('-created_at')[:8]
    print(assignments)
        
    
    context = {
        'tutor':tutor,
        'assignments':assignments,
    }
    return render(request,'tutors/homepage.html',context)

def profile_settings(request):
    tutor = Tutor.objects.get(user=request.user)
    user_form = UserForm(initial={'password':tutor.user.password,'confirm_password':tutor.user.password},instance=request.user)
    tutor_form = TutorForm(instance=tutor)
    if request.method == 'POST':
         user_form = UserForm(request.POST,instance=request.user)
         tutor_form = TutorForm(request.POST,request.FILES,instance=tutor)
         if user_form.is_valid() and tutor_form.is_valid():
            user_form.password = tutor.user.password
            user_form.confirm_password = tutor.user.password
            user_form.save()
            tutor_form.save()
            messages.success(request,'Your profile has been updated')
            return redirect('tutor_profile_settings')
         else:
            messages.error(request,'Something went wrong')
            print(user_form.errors)
            print(tutor_form.errors)

    context = {
        'user_form': user_form,
        'tutor_form': tutor_form,
        'tutor':tutor,
    }
    return render(request,'tutors/profile_settings.html',context)

def assignments(request):
    if request.method == 'GET':
        tutor = Tutor.objects.get(user=request.user)
        # get tutors location as GIS Point 
        pnt = GEOSGeometry('POINT(%s %s)' %(tutor.longitude,tutor.latitude), srid=4326)
        print(pnt)
        applied_assignments = tutor.applied_assignments.all()
        # filter assignments to be shown to tutor 
        # filter assignments by gender
        assignments = Assignment.objects.filter(Q(preferred_gender=tutor.gender) | Q(preferred_gender='NO PREFERENCE'))
        # filter assignments by tutor level 
        assignments = assignments.filter(preferred_tutor_level__in = [tutor.tutor_level])
        # filters assignments by subject
        assignments = assignments.filter(subject__in = tutor.subjects.all()).annotate(distance=Distance('student__location',pnt))
        
        for a in assignments:   
            a.kms = round(a.distance.km,2)       
        
        if request.GET.get('sort_by') == 'date_created':
            assignments = assignments.order_by('-created_at').annotate(distance=Distance('student__location',pnt))
            for a in assignments:   
                a.kms = round(a.distance.km,2)
            
        elif request.GET.get('sort_by') == 'hourly_rate':
            assignments = assignments.order_by('-hourly_rate').annotate(distance=Distance('student__location',pnt))
            for a in assignments:   
                a.kms = round(a.distance.km,2)
        elif request.GET.get('sort_by') == 'nearest':
            assignments = assignments.order_by('distance').annotate(distance=Distance('student__location',pnt))
            for a in assignments:   
                a.kms = round(a.distance.km,2)
        else:
            assignments = assignments.order_by('-created_at')
            for a in assignments:   
                a.kms = round(a.distance.km,2)
        

    context = {
        'tutor':tutor,
        'applied_assignments':applied_assignments,
        'assignments':assignments
    }
    return render(request,'tutors/assignments.html',context)

def apply_for_assignment(request,unique_id):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest': #check if it is a JsonRequest
        try:
            tutor = Tutor.objects.get(user=request.user)
            assignment = Assignment.objects.get(unique_id=unique_id)
            if tutor not in assignment.tutor.all():
                assignment.tutor.add(Tutor.objects.get(user=request.user))
                student = assignment.student
                user = request.user
                print('pre-email')
                send_assignment_application_email(request,user,student,assignment,tutor)
                print('post-email')
                sweetify.success(request, 'Successfully Applied for Assignment! Your contact details have been shared with the student, Good Luck!',timer=9000)
                return JsonResponse({'status':'SUCCESS','message':'Tutor Added to Applied','assignment':assignment.unique_id})
            else:
                assignment.tutor.remove(Tutor.objects.get(user=request.user))
                return JsonResponse({'status':'SUCCESS','message':'Tutor Removed'})
        except:
            return JsonResponse({'status':'Failed','message':'Something Went Wrong'})
                
 
    else:
        return JsonResponse({'status':'Failed','message':'Invalid Request'})
    