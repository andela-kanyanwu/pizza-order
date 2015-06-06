from django.db import models

# Create your models here.
class Pizza(models.Model):
    name = models.CharField(max_length=50, blank=False)
    price = models.PositiveIntegerField(blank=True)
    quantity_available = models.PositiveIntegerField(blank=False)