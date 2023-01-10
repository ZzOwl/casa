from django.db import models


class Booking(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    guest_count = models.IntegerField()
    reservation_time = models.DateField(auto_now=True)
    comments = models.CharField(max_length=1000)
    
    def __str__(self):
        return self.first_name






# class menu(models.Model):
#     menu_category_name = models.CharField(max_length=200)

# class menu_category(models.Model):
#     menu_item = models.CharField(max_length=40)
#     price = models.IntegerField(null=False)
#     category_id = models.ForeignKey(menu, on_delete=models.PROTECT, default=None, related_name='category_name')
    
    
# class customers(models.Model):    
#     id = models.PositiveIntegerField(primary_key = True)
#     email = models.EmailField(max_length=40)