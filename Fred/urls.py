from django.urls import path
from Fred.views import *
app_name = 'Fred'

urlpatterns = [
    path('',home,name='index'),
    path('contact',contact,name='contact'),
    path('about',about,name='about'),
    path('newsletter',newsletter,name='newsletter'),
    path('maintenance/', maintenance_mode, name='maintenance'),

]