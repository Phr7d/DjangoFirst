from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm


# Create your views here.

def login_view(request):
    if request.user.is_authenticated:
        return redirect('/')  # Redirect to home page if user is already logged in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return HttpResponse('Invalid username or password')
    form = AuthenticationForm()
    return render(request,'accounts/login.html', {'form': form})

def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('/')

def signup_view(request):
    return render(request,'accounts/signup.html')