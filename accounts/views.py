from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.urls import reverse
from .form import UserCreationForm
from django.core.mail import EmailMessage



# Create your views here.

def login_view(request):
    if request.user.is_authenticated:
        return redirect('/')  # Redirect to home page if user is already logged in
    if request.method == 'POST':
        #check if username is email or not
        if '@' in request.POST['username'] :
            email = request.POST['username']
            user = User.objects.get(email=email)
            user = user.username
            password = request.POST['password']
            user = authenticate(username=user, password=password)
        else :
            username = request.POST['username']
            print(username)
            password = request.POST['password']
            user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return render(request,'accounts/login.html',{'error': True})
    return render(request,'accounts/login.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('/')


def signup_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            print(form.is_valid())
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password1')
                user = authenticate(username=username, password=password)
                email = form.cleaned_data.get('email')
                email = EmailMessage('Create User',f"Hello {username}.\nWelcome to our site", to=[email])
                email.send()
                login(request, user)
                return redirect('/')
        form = UserCreationForm()
        context = {'form': form}
        return render(request,'accounts/signup.html',context)
    else :
        return redirect('/')


def forget_password_view(request):
    if request.user.is_authenticated:
        return redirect('/')  # Redirect to home page if user is already logged in
    if request.method == 'POST':
        email = request.POST['email']
        try:
            user = User.objects.get(email=email)
            new_password = User.objects.make_random_password()
            user.set_password(new_password)
            print(new_password) # Save the new password to the database.
            user.save()
            email = EmailMessage('Password Change',f"New Password is : {new_password} ", to=[email])
            email.send()
            # send email notification
            return render(request,'accounts/login.html') 
        except User.DoesNotExist:
            print('User does not exist')
            return render(request,'accounts/forget-password.html',{'error': True})
    return render(request,'accounts/forget-password.html')