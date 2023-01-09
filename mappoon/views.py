from django.shortcuts import render
# from django.http import HttpResponse

#from django.views import View     #for class based views
from mappoon.forms import BookingForm


def form_view(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
    context = {"form" : form}
    return render(request, "home.html", context)
    
''' 
class MyView(View):
    def get(self, request):
    ...
    pass
    
    
    def post(self, request):
    ...
    pass
'''