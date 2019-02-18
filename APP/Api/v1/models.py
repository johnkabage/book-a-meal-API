from werkzeug.security import generate_password_hash
from datetime import datetime

users = []
meal_orders = []

class MealOrder:
    meal_id = 1
    def __init__(self, city, area, meal, quantity, price, receiver):
        self.city = city
        self.area = area
        self.meal = meal
        self.quantity = quantity
        self.price = price
        self.receiver = receiver
        self.date = str(datetime.now())
        self.id = MealOrder.meal_id

        MealOrder.meal_id += 1

    def get_meal_by_id(self, id):
        for meal in meal_orders:
            if meal.id == id:
                return meal

    def get_meal_by_user(self,user):
        users_meal = [meal for meal in meal_orders if meal.user == user]
        return users_meal

class User:
    user_id = 1
    def __init__(self, fname, lname, username, email, password, confirm_password):
        self.fname = first_name
        self.lname = last_name
        self.username = username
        self.email = email
        if password:
            self.password = generate_password_hash(password)
        if confirm_password:
            self.confirm_password = generate_password_hash(confirm_password)
        self.id = User.

    def get_user_by_username(self, user):
        for user in users:
            if user.id == id:
                return user

    def get_user_by_id(self, id):
        for user in users:
            if user.id == id:
                return user

    def serialize(self):
        return dict(
            id = self.id
            username = self.username
            email = self.email
        )



