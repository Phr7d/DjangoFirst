from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User



# Create your views here.

def login_view(request):
    if request.user.is_authenticated:
        return redirect('/')  # Redirect to home page if user is already logged in
    if request.method == 'POST':
        #check if username is email or not
        if '@' in request.POST['username'] :
            email = request.POST['username']
            username = User.objects.get(email=email)
            username = username.username
            password = request.POST['password']
            user = authenticate(username=username, password=password)
        else :
            username = request.POST['username']
            print(username)
            password = request.POST['password']
            user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return HttpResponse('Invalid username or password')
    return render(request,'accounts/login.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('/')


def signup_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password1')
                user = authenticate(username=username, password=password)
                login(request, user)
                return redirect('/')
        form = UserCreationForm()
        context = {'form': form}
        return render(request,'accounts/signup.html',context)
    else :
        return redirect('/')