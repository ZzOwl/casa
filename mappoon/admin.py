from django.contrib import admin

from .models import menu
from .models import menu_cat
from .models import customers

admin.site.register(menu)
admin.site.register(menu_cat)
admin.site.register(customers)