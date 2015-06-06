from django.forms import widgets
from rest_framework import serializers
from pizza_app.models import Pizza

class PizzaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pizza
        fields = ('name', 'price', 'quantity_available')