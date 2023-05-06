from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Student
from accounts.forms import UserForm, StudentForm
from assignments.forms import AssignmentForm
from assignments.models import Assignment
from django.contrib import messages
from .utils import key_generator
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
            messages.success(request,'Assignment Created Successfully')
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