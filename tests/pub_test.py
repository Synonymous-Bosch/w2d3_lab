import unittest
from src.pub import Pub
from src.drink import Drink
from src.customer import Customer
from src.food import Food

class TestPub(unittest.TestCase):
    def setUp(self):

        self.customer1 = Customer("Leonardo", 30, 19, 1)
        self.customer2 = Customer("Donatello", 80, 17, 1)
        self.customer3 = Customer("Michaelangelo", 20, 18, 5)
        self.drink1 = Drink("pint", 1.00, 1)
        self.drink2 = Drink("red wine", 3.00, 1)
        drinks = {self.drink1: 50, self.drink2: 20}
        self.food = Food("pizza", 5.00, 1)
        foods = [self.food]
        self.pub = Pub("The Prancing Pony", 100.00, drinks, foods)

        

    def test_pub_has_name(self):
        self.assertEqual("The Prancing Pony", self.pub.name)

    def test_pub_has_till_value(self):
        self.assertEqual(100, self.pub.till)

    def test_increase_till(self):
        self.pub.increase_till(2.50)
        self.assertEqual(102.50, self.pub.till)

    def test_buy_drink(self):
        drink = self.pub.find_drink_by_name("pint")
        self.pub.buy_drink(self.customer1, drink)
        self.assertEqual(29.00, self.customer1.wallet)
        self.assertEqual(101.00, self.pub.till)
        self.assertEqual(2, self.customer1.drunkenness)

    def test_find_drink_by_name(self):
        drink = self.pub.find_drink_by_name("pint")
        self.assertEqual("pint", drink.name)

    def test_check_customer_age_true(self):
        result = self.pub.check_customer_age(self.customer1)
        self.assertEqual(True, result)

    def test_check_customer_age_false(self):
        result = self.pub.check_customer_age(self.customer2)
        self.assertEqual(False, result)

    def test_buy_drink_age_false(self):
        drink = self.pub.find_drink_by_name("pint")
        self.pub.buy_drink(self.customer2, drink)
        self.assertEqual(80.00, self.customer2.wallet)
        self.assertEqual(100.00, self.pub.till)

    def test_check_drunkenness_false(self):
        result = self.pub.check_drunkenness(self.customer3)
        self.assertEqual(False, result)

    def test_check_drunkenness_true(self):
        result = self.pub.check_drunkenness(self.customer1)
        self.assertEqual(True, result)  

    def test_buy_drink_drunk_false(self):
        drink = self.pub.find_drink_by_name("pint")
        self.pub.buy_drink(self.customer3, drink)
        self.assertEqual(20.00, self.customer3.wallet)
        self.assertEqual(100.00, self.pub.till)

    def test_find_food_by_name(self):
        food = self.pub.find_food_by_name("pizza")
        self.assertEqual("pizza", food.name)

    def test_buy_food(self):
        self.pub.buy_food(self.customer3, "pizza")
        self.assertEqual(15.00, self.customer3.wallet)
        self.assertEqual(105.00, self.pub.till)
        self.assertEqual(4, self.customer3.drunkenness)

    def test_stock_value(self):
        result = self.pub.stock_value(self.pub.drinks)
        self.assertEqual(110.00, result)