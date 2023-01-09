from django import forms

from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'




# from django.forms.widgets import NumberInput    #for reservation_date

# class DemoForm(forms.Form):
#     name = forms.CharField(widget=forms.Textarea(attrs={'rows':5}), label='enter name', max_length=50)  # attr will determine the size of the field
#     age = forms.IntegerField(min_value=20, max_value=60)
#     email = forms.EmailField(label='enter the Email')            #label text will replace the email
#     reservation_date = forms.DateField(widget=NumberInput(attrs={'type' : 'date'}))
#     reservation_time = forms.TimeField(required=False)