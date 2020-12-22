from django.db import models

class ClientOrder(models.Model):
    name = models.CharField(max_length=20)
    phone_number = models.IntegerField()
    location = models.CharField(max_length=20)
    price = models.IntegerField()
    email = models.EmailField()
    description = models.TextField(blank=True, null=True)
    # order_name = models.CharField(max_length=20)
