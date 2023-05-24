from src.customer import Customer
from src.drink import Drink
from src.food import Food
import pdb

class Pub:
    def __init__(self, name, till, drinks, foods):
        self.name = name
        self.till = till
        self.drinks = drinks
        self.foods = foods
        

    def increase_till(self, amount):
        self.till += amount

    def check_customer_age(self, customer):
        if customer.age >= 18:
            return True
        else: 
            return False
        
    def get_drink_price(drink):
        return drink.price

    def buy_drink(self, customer, drink):
        if self.check_customer_age(customer) == True and self.check_drunkenness(customer) == True:
            price = drink.price
            customer.decrease_wallet(price)
            self.increase_till(price)
            customer.drunkenness += drink.alcohol_level
            self.drinks[drink] += 1
        else:
            print("No booze for you")

    def find_drink_by_name(self, drink_name):
        drinks_list = list(self.drinks)
        for drink in drinks_list:
            if drink_name == drink.name:
                return drink
            
    def check_drunkenness(self, customer):
        if customer.drunkenness <4:
            return True
        else: 
            return False
            
        
    def find_food_by_name(self, food_name):
        for food in self.foods:
            if food_name == food.name:
                return food
    
    def buy_food(self, customer, food_name):
        food = self.find_food_by_name(food_name)
        price = food.price
        customer.decrease_wallet(price)
        self.increase_till(price)
        customer.drunkenness -= food.rejuvenation_level

    def stock_value(self, drinks):
        total_value = 0
        for drink in drinks.items():
            total_value += drink[0].price * drink[1]
        return total_value
