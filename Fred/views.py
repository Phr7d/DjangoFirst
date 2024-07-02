from django.shortcuts import render
from django.http import HttpResponse
from Fred.forms import *

# Create your views here.

def contact(request):
    # return render(request,'index.html')
    return render(request,'website/contact.html')

def about(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            print('Done')
        else:
            print('notDone')
    form = ContactForm()
    # return render(request,'index.html')
    return render(request,'website/about.html',{'form':form})

def home(request):
    # return render(request,'index.html')
    return render(request,'website/index.html')




