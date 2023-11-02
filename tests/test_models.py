from django.test import TestCase
from restaurant.models import Menu

class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="IceCream", price=80, inventory=200)
        # print('printing')
        # print(item)
        self.assertEqual(str(item), "IceCream : 80")

class MenuTestMultiple(TestCase):
    def setUp(self):
        self.bagel = Menu.objects.create(title="bagel", price=34, inventory=50)
        self.pizza = Menu.objects.create(title="pizza", price=23, inventory=20)
        self.noodles = Menu.objects.create(title="noodles", price=34, inventory=10)
    def test_getall(self):
        self.assertEqual(str(self.bagel), "bagel : 34")
        self.assertEqual(str(self.pizza), "pizza : 23")
        self.assertEqual(str(self.noodles), "noodles : 34")
        