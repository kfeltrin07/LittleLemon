from django.test import TestCase
from restaurant.models import MenuItem
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient
from restaurant.serializers import MenuItemSerializer
import json

class MenuViewTest(TestCase):
    def setup(self):
        self.menu1 = MenuItem.objects.create(Title="HotChocolate", Price=30, Inventory=100)
        self.menu2 = MenuItem.objects.create(Title="Pizza", Price=67, Inventory=50)
        self.menu3 = MenuItem.objects.create(Title="Coffe", Price=20, Inventory=200)

    def test_getall(self):
        response = self.client.get('/restaurant/menu/items/')
        items = MenuItem.objects.all()
        serializer = MenuItemSerializer(items, many=True)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content), serializer.data)