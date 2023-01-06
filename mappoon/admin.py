from django.contrib import admin

from .models import menu
from .models import menu_category
from .models import customers

admin.site.register(menu)
admin.site.register(menu_category)
admin.site.register(customers)