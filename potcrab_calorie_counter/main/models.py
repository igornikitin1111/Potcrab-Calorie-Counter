from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext
from django.utils.translation import gettext_lazy as _

# Create your models here.
class UserCalorieCounter(AbstractUser):
    CREATE TABLE IF NOT EXISTS User (
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        username INTEGER NOT NULL,
        email INTEGER NOT NULL,
        current_weight INTEGER NOT NULL,
        current_calorie_goal INTEGER NOT NULL
    );

    CREATE TABLE IF NOT EXISTS user_weight (
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        user_id INTEGER NOT NULL,
        weight DECIMAL NOT NULL,
        date DATETIME NOT NULL,
        FOREIGN KEY (user_id) REFERENCES User(id)
    );

    CREATE TABLE IF NOT EXISTS user_calorie_goals (
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        user_id INTEGER NOT NULL,
        calorie_goal DECIMAL NOT NULL,
        datetime DATETIME NOT NULL,
        FOREIGN KEY (user_id) REFERENCES User(id)
    );

    CREATE TABLE IF NOT EXISTS user_calories (
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        user_id INTEGER NOT NULL,
        calories DECIMAL NOT NULL,
        calories_total_per_day DECIMAL NOT NULL,
        datetime DATETIME NOT NULL,
        FOREIGN KEY (user_id) REFERENCES User(id)
    );

    CREATE TABLE IF NOT EXISTS food_product (
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        name FLOAT NOT NULL,
        category FLOAT NOT NULL,
        portion_weight DECIMAL NOT NULL,
        calories DECIMAL NOT NULL,
        protein DECIMAL NOT NULL,
        fat DECIMAL NOT NULL,
        carbohydrates DECIMAL NOT NULL
    );

    CREATE TABLE IF NOT EXISTS dish_with_recipe (
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        name FLOAT NOT NULL,
        category FLOAT NOT NULL,
        portion_weight DECIMAL NOT NULL,
        calories DECIMAL NOT NULL,
        protein DECIMAL NOT NULL,
        fat DECIMAL NOT NULL,
        carbohydrates DECIMAL NOT NULL,
        recipe TEXT NOT NULL
    );

    CREATE TABLE IF NOT EXISTS food_log (
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        user_id INTEGER NOT NULL,
        selected_food_amount DECIMAL NOT NULL,
        total_calories DECIMAL NOT NULL,
        total_protein DECIMAL NOT NULL,
        total_fat DECIMAL NOT NULL,
        total_carbohydrates DECIMAL NOT NULL,
        food_name FLOAT NOT NULL,
        food_weight DECIMAL NOT NULL,
        food_calories DECIMAL,
        food_protein DECIMAL,
        food_fat DECIMAL,
        food_carbohydrates DECIMAL,
        dish_name FLOAT,
        dish_weight DECIMAL,
        dish_calories DECIMAL,
        dish_protein DECIMAL,
        dish_fat DECIMAL,
        dish_carbohydrates DECIMAL,
        FOREIGN KEY (user_id) REFERENCES User(id),
        FOREIGN KEY (food_name) REFERENCES food_product(id),
        FOREIGN KEY (food_weight) REFERENCES food_product(id),
        FOREIGN KEY (food_calories) REFERENCES food_product(id),
        FOREIGN KEY (food_protein) REFERENCES food_product(id),
        FOREIGN KEY (food_fat) REFERENCES food_product(id),
        FOREIGN KEY (food_carbohydrates) REFERENCES food_product(id),
        FOREIGN KEY (dish_name) REFERENCES dish_with_recipe(id),
        FOREIGN KEY (dish_weight) REFERENCES dish_with_recipe(id),
        FOREIGN KEY (dish_calories) REFERENCES dish_with_recipe(id),
        FOREIGN KEY (dish_protein) REFERENCES dish_with_recipe(id),
        FOREIGN KEY (dish_fat) REFERENCES dish_with_recipe(id),
        FOREIGN KEY (dish_carbohydrates) REFERENCES dish_with_recipe(id)
    );