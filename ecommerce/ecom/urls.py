from django.urls import path,include 
from . import views

urlpatterns = [

    path('',views.index,name='Home'),
    path('about',views.about,name='About'),
    path('department',views.department,name='Department')
]
