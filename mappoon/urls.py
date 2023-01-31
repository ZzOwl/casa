from django.urls import re_path   #dynamic pages
from django.urls import path      #static pages
from . import views

urlpatterns =[
    path('booking/', views.form_view),
    path('home/<name>/', views.home),
    #path('', views.ClassName.as_view() , name='my-view'),    #as_view is for class based views
]