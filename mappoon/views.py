from django.shortcuts import render
from django.http import HttpResponse

#from django.views import View     #for class based views
from .forms import DemoForm


def get(request):
    form = DemoForm()
    context = {'form': form}
    return HttpResponse(render(request, 'home.html', context))
    
''' 
class MyView(View):
    def get(self, request):
    ...
    pass
    
    
    def post(self, request):
    ...
    pass
'''