from django.shortcuts import render

from django.http import HttpResponse
from django.views import View

class MyView(View):
    def get(self, request):
        return HttpResponse('get')
    
    def post(self, request):
        return HttpResponse('post')
    
