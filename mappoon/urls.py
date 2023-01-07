from django.urls import re_path   #dynamic pages
from django.urls import path      #static pages
from . import views

urlpatterns =[
    path('', views.MyView.as_view() , name='my-view'),
]