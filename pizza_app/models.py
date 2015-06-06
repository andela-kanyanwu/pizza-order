from django.db import models

class Pizza(models.Model):
    name = models.CharField(max_length=50, blank=False)
    price = models.PositiveIntegerField(blank=False)
    quantity_available = models.PositiveIntegerField(blank=False)