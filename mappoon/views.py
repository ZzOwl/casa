from django.shortcuts import render
from django.http import HttpResponse

from django.views import View
from .forms import DemoForm

class MyView(View):
    def get(self, request):
        return HttpResponse('get')
    
    def post(self, request):
        form = DemoForm()
        context = {'form': form}
        return render(request, 'home.html', context) 
    
