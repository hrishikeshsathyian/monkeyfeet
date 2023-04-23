from django.shortcuts import render, redirect
from .forms import UserForm,StudentForm
from .models import User
from student.models import Student
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator
from .utils import send_account_activation_email
from django.contrib.auth import logout as auth_logout

# Create your views here.
def login(request):
    if request.method == 'POST':
        # retrieve email and password from login form
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request,email=email,password=password)
        if user is not None: # if user is not active it will also return None
            auth_login(request,user)
            messages.success(request,'Successfully logged in')
            if user.role == User.STUDENT:
                return redirect('student_homepage')
            else:
                pass # redirect to tutor homepage
            
        else:
            if User.objects.filter(email=email).exists(): # check if email exists
                user = User.objects.get(email=email)
                if not user.is_active: # check if error is rising from user not being activated
                    messages.error(request,'Please click the link in your email to activate your account')
                else:
                    messages.error(request,'Incorrect Password')
            else:
                messages.error(request,'Account with that email does not exist')
            return redirect('login')
    return render(request,'accounts/login.html')

# register new user as a tutor
def register_tutor(request):
    return render(request,'accounts/register_tutor.html')

# register new user as a student
def register_student(request):
    user_form = UserForm()
    student_form = StudentForm()
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        student_form = StudentForm(request.POST,request.FILES)
        if user_form.is_valid() and student_form.is_valid():
            password = user_form.cleaned_data['password']
            user = user_form.save(commit=False)
            user.role = User.STUDENT
            user.set_password(password)
            user.save()
            instance = Student.objects.get(user=user)
            student = StudentForm(request.POST,request.FILES,instance=instance)
            student.save()
            send_account_activation_email(request,user)
            messages.success(request,'Account has been successfully created!An email has been sent to you for verification')
            return redirect('login')
        else:
            print(user_form.errors)
            print(student_form.errors)
            
   
    context = {
        'user_form':user_form,
        'student_form':student_form,
    }
    return render(request,'accounts/register_student.html',context)


def activate(request,uidb64,token):
    #Activate the user by setting the is_active status to true
    try:
        uid = urlsafe_base64_decode(uidb64).decode() #decodes the previosuly encoded uid base 64 back to user id so we can retrieve user
        user = User._default_manager.get(pk=uid)
    except(TypeError,ValueError,OverflowError,User.DoesNotExist):
        user = None
    if user is not None and default_token_generator.check_token(user,token):
        user.is_active = True
        user.save()
        messages.success(request,"Congratulations your account is activated")
        return redirect('login')
    else:
        messages.error(request,"Invalid activation link")
        return redirect('login')
    

def logout(request):
    auth_logout(request)
    messages.info(request,'You are logged out!')
    return redirect('login')