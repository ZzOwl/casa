from django.contrib import admin

from .models import Booking
admin.site.register(Booking)

from django.contrib.auth.models import User
# admin.site.unregister(User)

# from django.contrib.auth.admin import UserAdmin 
# @admin.register(User) 
# class NewAdmin(UserAdmin): 
#     def get_form(self, request, obj=None, **kwargs): 
#         form = super().get_form(request, obj, **kwargs) 
#         is_superuser = request.user.is_superuser 
#         if not is_superuser: 
#             form.base_fields['username'].disabled = True 

#         return form

   
