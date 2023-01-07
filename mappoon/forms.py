from django import forms
from django.forms.widgets import NumberInput    #for reservation_date

class DemoForm(forms.Form):
    name = forms.CharField(widget=forms.Textarea(attrs={'rows':5}), label='enter name', max_length=50)  # attr will determine the size of the field
    email = forms.EmailField(label='enter the Email')            #label text will replace the email
    reservation_date = forms.DateField(widget=NumberInput(attrs={'type' : 'date'}))
    
    DISH_LIST = [
        ('italian', 'Italian')
        ('greek', 'Greek')                  #for favorite_dish
        ('chinese', 'Chinese')
    ]
    
    favorite_dish = forms.ChoiceField(widget=forms.RadioSelect, choices= DISH_LIST)      #by using radio select all choices will be shown at once
    age = forms.IntegerField(min_value=20, max_value=60)
    #some other fields:  FileField  &   MultipleChoiceField