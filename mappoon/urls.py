from django.urls import re_path   #dynamic pages
from django.urls import path      #static pages
from django.contrib import admin
from . import views

urlpatterns =[
    path('', views.MyView.as_view() , name='my-view'),
    path('home/', views.MyView.post)
]