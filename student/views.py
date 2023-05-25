from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Student
from tutors.models import Tutor
from accounts.forms import UserForm, StudentForm
from assignments.forms import AssignmentForm
from assignments.models import Assignment
from django.contrib import messages
from .utils import key_generator
from django.db.models import Q
from django.contrib.gis.geos import GEOSGeometry
from django.contrib.gis.measure import D
from django.contrib.gis.db.models.functions import Distance
import sweetify
# Create your views here.

def homepage(request):
    student = Student.objects.get(user = request.user) # get logged in student
    context = {
        'student': student,
    }
    return render(request,'student/homepage.html',context)

def about(request):
    return render(request,'student/about.html')

def assignments(request):
    student = Student.objects.get(user=request.user)
    form = AssignmentForm(initial={'additional_information':student.additional_information})
    form.fields['subject'].queryset = student.subjects.all()

    if request.method == 'POST':
        form = AssignmentForm(request.POST)
        
        if form.is_valid(): # check if form is valid, field validators
            assignment = form.save(commit=False)
            assignment.student = student      
            assignment.address = student.address
            assignment.preferred_gender = student.preferred_gender
            assignment.save()
            assignment.preferred_tutor_level.set(val for val in student.preferred_tutor_level.all()) # sets many to many field
            assignment.save()
            sweetify.success(request, 'Assignment successfully created! If any tutors apply, their contact information will be shared with you via email :)',timer=9000)
            return redirect('assignments')
        else:
            print(form.errors)
    assignments = Assignment.objects.filter(student=student)
    
    context = {
        'form':form,
        'student':student,
        'assignments':assignments
        }
    return render(request,'student/assignments.html',context)

def delete_assignment(request,unique_id):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest': #check if it is a JsonRequest
        try:
            assignment = Assignment.objects.get(unique_id=unique_id)
            assignment.delete()
            return JsonResponse({'status':'SUCCESS','message':'Assignment Deleted','assignment':assignment.unique_id})
        except:
            return JsonResponse({'status':'Failed','message':'Assignment Does Not Exist'})
                
 
    else:
        return JsonResponse({'status':'Failed','message':'Invalid Request'})
   

def tutors(request):

    student = Student.objects.get(user=request.user)
    applied_tutors = student.applied_tutors.all()
    pnt = GEOSGeometry('POINT(%s %s)' %(student.longitude,student.latitude), srid=4326)
    print(pnt)
    print(student.address)
    tutors = Tutor.objects.filter(subjects__in=student.subjects.all()).distinct()
    tutors = tutors.filter(tutor_level__in=student.preferred_tutor_level.all()).distinct()
    
    if student.preferred_gender == 'NO PREFERENCE':
        tutors = tutors.annotate(distance=Distance('location',pnt))
    else:
        tutors = tutors.filter(gender=student.preferred_gender).annotate(distance=Distance('location',pnt))
    for t in tutors:   
            t.kms = round(t.distance.km,2)    

    print(tutors)
    context = {
        'tutors': tutors,
        'student': student,
        'applied_tutors': applied_tutors,
    }
    return render(request,'student/tutors.html',context)

def profile_settings(request):
    student = Student.objects.get(user=request.user)
    user_form = UserForm(initial={'password':student.user.password,'confirm_password':student.user.password},instance=request.user)
    student_form = StudentForm(instance=student)
    if request.method == 'POST':
        user_form = UserForm(request.POST,instance=request.user)
        student_form = StudentForm(request.POST,request.FILES,instance=student)
        if user_form.is_valid() and student_form.is_valid():
            user_form.password = student.user.password
            user_form.confirm_password = student.user.password
            user_form.save()
            student_form.save()

            messages.success(request,'Your profile has been updated')
            return redirect('profile_settings')
        else:
            messages.error(request,'Something went wrong')
            print(user_form.errors)
            print(student_form.errors)

    context = {
        'user_form': user_form,
        'student_form': student_form,
        'student':student,
    }
    return render(request,'student/profile_settings.html',context)