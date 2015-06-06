from django.shortcuts import render
from django.http import Http404

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from pizza_app.models import Pizza
from pizza_app.serializers import PizzaSerializer


class PizzaList(APIView):
    """
    List all pizzas, or create a new pizza.
    """  
    serializer_class = PizzaSerializer
    def get(self, request, format=None):
        pizzas = Pizza.objects.all()
        serializer = PizzaSerializer(pizzas, many=True)
        return Response(serializer.data)

    def post(self, request, format=None): 
        serializer = PizzaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PizzaDetail(APIView):
    """
    Retrieve, update or delete a pizza instance.
    """
    serializer_class = PizzaSerializer
    def get_object(self, name):  
        try:
            return Pizza.objects.get(name__iexact=name)
        except Pizza.DoesNotExist:
            raise Http404

    def get(self, request, name, format=None):
        pizza = self.get_object(name)
        serializer = PizzaSerializer(pizza)
        return Response(serializer.data)

    def put(self, request, name, format=None):
        pizza = self.get_object(name)
        serializer = PizzaSerializer(pizza, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, name, format=None):
        pizza = self.get_object(name)
        pizza.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)