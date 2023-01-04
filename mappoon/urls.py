from django.urls import path
from . import MyView

urlpatterns =[
    path('', MyView.as_view() , name='my-view'),
]