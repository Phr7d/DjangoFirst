from django.urls import path
from Fred.views import *

app_name = 'Shahin'

urlpatterns = [
    path('contact',contact,name='contact'),
    path('about',about,name='about'),
    path('',home,name='index'),
    path('test',test_view,name='test'),
]