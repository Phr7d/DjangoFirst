from django.urls import path
from Fred.views import *

app_name = 'Fred'

urlpatterns = [
    path('contact',contact,name='contact'),
    path('about',about,name='about'),
    path('',home,name='index'),

]