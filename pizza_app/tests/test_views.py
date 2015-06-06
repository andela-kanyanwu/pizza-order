from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from pizza_app.models import Pizza


class PizzaListTest(APITestCase):
    url = reverse('pizza_list')
    def setUp(self):
        Pizza.objects.create(name="beef", price=50, quantity_available=10)

    def test_get_pizzas(self):
        """
        Ensure we can get all the pizza objects.
        """
        data = [{"name": "beef", "price": 50, "quantity_available": 10}]
        response = self.client.get(self.url)
        self.assertEqual(response.data, data)

    def test_get_all_pizzas_when_no_data_is_available(self):
        Pizza.objects.all().delete()
        data = []
        response = self.client.get(self.url)
        self.assertEqual(response.data, data)

    def test_post_pizza(self):
        """
        Ensure we can create a new pizza object.
        """
        data = {"name": "cheese", "price": 30, "quantity_available": 10}
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data, data)

    def test_post_pizza_with_empty_field(self):
        """
        Ensure we cannot post pizza with empty field.
        """
        data = {"name": '', "price": '', "quantity_available": ''}
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.data, {'price': ['A valid integer is required.'], 'name': ['This field may not be blank.'], 'quantity_available': ['A valid integer is required.']})

class PizzaDetailTest(APITestCase):
    url = reverse('pizza_detail', kwargs={"name": "beef"})
    def setUp(self):
        Pizza.objects.create(name="beef", price=50, quantity_available=10)

    def test_get_pizza(self):
        """
        Ensure we can get details of a new pizza object.
        """
        data = {"name": "beef", "price": 50, "quantity_available": 10}
        response = self.client.get(self.url)
        self.assertEqual(response.data, data)

    def test_get_pizza_when_no_data_is_available(self):
        Pizza.objects.all().delete()
        data = {'detail': 'Not found.'}
        response = self.client.get(self.url)
        self.assertEqual(response.data, data)

    def test_put_pizza(self):
        """
        Ensure we can edit a pizza object.
        """
        data = {"name": "beef", "price": 50, "quantity_available": 10}
        response = self.client.put(self.url, data, format='json')
        self.assertEqual(response.data, data)

    def test_delete_pizza(self):
        """
        Ensure we can delete a pizza object.
        """
        data = {"name": "beef", "price": 50, "quantity_available": 10}
        response = self.client.delete(self.url)
        self.assertEqual(response.data, None)