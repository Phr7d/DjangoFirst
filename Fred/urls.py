from django.urls import path
from Fred.views import contact,about,home
urlpatterns = [
    path('contact',contact),
    path('about',about),
    path('',home),
]