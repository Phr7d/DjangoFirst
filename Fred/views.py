from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from Fred.forms import *
from Fred.models import *



def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.name = 'unknown'
            instance.save()
            return render(request,'website/contact.html',{'form':form, 'success': True})
        else:
            return render(request,'website/contact.html',{'form':form, 'error': True})
        
    else :
        form = ContactForm()
        return render(request,'website/contact.html',{'form':form})

def newsletter(request):
    if request.method == 'POST':
        form = NewsLetterFrom(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'website/index.html',{'form':form, 'success': True})
        else:
            return render(request,'website/index.html',{'form':form, 'error': True})

def about(request):
    # return render(request,'index.html')
    return render(request,'website/about.html')

def home(request):
    # return render(request,'index.html')
    return render(request,'website/index.html')


def maintenance_mode(request):
    return render(request, 'website/maintenance.html')