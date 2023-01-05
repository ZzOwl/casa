from django.db import models



class menu(models.Model):
    menu_cat_name = models.CharField(max_length=200)

class menu_cat(models.Model):
    menu_item = models.CharField(max_length=40)
    price = models.IntegerField(null=False)
    cat_id = models.ForeignKey(menu, on_delete=models.PROTECT, default=None)
    
class customers(models.Model):    
    id = models.PositiveIntegerField(primary_key = True)
    email = models.EmailField(max_length=40)