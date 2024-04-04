from django.test import TestCase
from restaurant.models import MenuItem

class MenuItemTest(TestCase):
    def test_get_item(self):
        item = MenuItem.objects.create(Title="IceCream", Price=80, Inventory=100)
        itemstr = item.__str__()
        self.assertEqual(itemstr, "IceCream : 80")   