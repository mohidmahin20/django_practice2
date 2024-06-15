from django.urls import path,include
from . import views

urlpatterns = [
    path('about/',views.about, name='about_us'),
    
    
]
