from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def contact(request):
    # return render(request,'index.html')
    return render(request,'website/contact.html')

def about(request):
    # return render(request,'index.html')
    return render(request,'website/about.html')

def home(request):
    # return render(request,'index.html')
    return render(request,'website/index.html')




