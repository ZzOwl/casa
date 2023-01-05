from django.db import models


#model for menues
#model for sub menues


class people(models.Model):
    id = models.PositiveIntegerField(primary_key = True)
    name = models.CharField(max_length=40)
    email = models.EmailField(max_length=40)
    phone = models.IntegerField()
