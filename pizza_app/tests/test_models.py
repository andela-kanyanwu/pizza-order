from django.test import TestCase
from pizza_app.models import Pizza


class PizzaTests(TestCase):
    def setUp(self):
        Pizza.objects.create(name="beef", price=50, quantity_available=10)

    def test_pizza_model(self):
        pizza = Pizza.objects.get(name="beef", price=50, quantity_available=10)
        self.assertEqual(pizza.name, "beef")
        self.assertEqual(pizza.price, 50)
        self.assertEqual(pizza.quantity_available, 10)
