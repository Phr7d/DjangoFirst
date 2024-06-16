from django.urls import path
from Fred.views import Contact,Home,Index
urlpatterns = [
    path('Contact',Contact),
    path('Home',Home),
    path('',Index),
]