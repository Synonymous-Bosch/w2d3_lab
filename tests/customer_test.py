import unittest
from src.pub import Pub
from src.drink import Drink
from src.customer import Customer
from src.food import Food

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer1 = Customer("Leonardo", 30, 19, 1)
        self.customer2 = Customer("Donatello", 80, 17, 5)



    def test_decrease_wallet(self):
        self.customer1.decrease_wallet(1.20)
        self.assertEqual(28.80, self.customer1.wallet)


        




