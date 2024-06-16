from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def Contact(request):
    return HttpResponse("<h1>Contactsssss</h1>")
def Home(request):
    return HttpResponse("<h1>Homeeeeme</h1>")
def Index(request):
    return HttpResponse("<h1>Indexxxxxx</h1>")