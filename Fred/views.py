from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def contact(request):
    # return render(request,'index.html')
    return render(request,'website/contact.html')

def Home(request):
    return HttpResponse("<h1>Homeeeeme</h1>")

def Index(request):
    return HttpResponse("<h1>Indexxxxxx</h1>")