from django.urls import path
from .import views
urlpatterns = [
     path('',views.view_meal,name='show_item'),
     
]
