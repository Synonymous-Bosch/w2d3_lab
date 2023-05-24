import unittest
from src.pub import Pub
from src.drink import Drink
from src.customer import Customer
from src.food import Food

class TestDrink(unittest.TestCase):
    def setUp(self):
        self.drink1 = Drink("pint", 1.00, 1)

    def test_get_drink_price(self):
        self.assertEqual(1.00, self.drink1.price)