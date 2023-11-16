from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext
from django.utils.translation import gettext_lazy as _

# Create your models here.

class User(models.Model):
    username = models.CharField(_("Username"), max_length=50)
    email = models.EmailField(_("E-mail"), max_length=254)
    first_name = models.CharField(_("First name"), max_length=50)
    last_name = models.CharField(_("Last name"), max_length=50)
    # gender = 
    height = models.DecimalField(_("Height (cm)"), max_digits=7, decimal_places=2)
    weight = models.DecimalField(_("Weight (kg)"), max_digits=7, decimal_places=2)


class UserWeight(models.Model):
    user = models.ForeignKey(
        User, 
        verbose_name=_("user"), 
        related_name='user',
        on_delete=models.CASCADE,
    )
    weight = models.DecimalField(_("weight"), max_digits=5, decimal_places=2)
    created_at = models.DateTimeField(_("created at"), auto_now_add=True, db_index=True)


#class UserWeightGoal(models.Model):
#   pass


class UserCalories(models.Model):
    user = models.ForeignKey(
        User, 
        verbose_name=_("user"), 
        on_delete=models.CASCADE
    )
    calories = models.DecimalField(_("Calories"), max_digits=7, decimal_places=2)
    created_at = models.DateTimeField(_("created at"), auto_now_add=True, db_index=True)
#   calories_total_per_day DECIMAL NOT NULL,


# class UserCalorieGoal(models.Model):
#     user = models.ForeignKey(
#         User, 
#         verbose_name=_("user"), 
#         on_delete=models.CASCADE
#     )
#     calorie_goal = models.DecimalField(_("Calorie goal"), max_digits=7, decimal_places=2)
#     created_at = models.DateTimeField(_("created at"), auto_now_add=True, db_index=True)


class FoodCategory(models.Model):
    name = models.CharField(_("name"), max_length=50)

    def __str__(self):
        return self.name


class Food(models.Model):
    name = models.CharField(_("Name"), max_length=50)
    category = models.ForeignKey(
        FoodCategory, 
        verbose_name=_("Category"),
        related_name="food", 
        on_delete=models.CASCADE,
        null=True
    )
    portion_weight = models.DecimalField(_("Portion weight (g)"), max_digits=7, decimal_places=2)
    calories = models.DecimalField(_("Calories"), max_digits=7, decimal_places=2)
    protein = models.DecimalField(_("Protein"), max_digits=7, decimal_places=2)
    fat = models.DecimalField(_("Fat"), max_digits=7, decimal_places=2)
    carbohydrates = models.DecimalField(_("Carbohydrates"), max_digits=7, decimal_places=2)
    recipe = models.TextField(_("Recipe"), null=True, blank=True)
    food_image = models.ImageField(null=True, blank=True, upload_to="food/")

    def __str__(self):
        return self.name


# class FoodLog(models.Model):
#     user = models.ForeignKey(
#         User, 
#         verbose_name=_("user"), 
#         on_delete=models.CASCADE
#     )
#     selected_food_amount = models.DecimalField(_("Selected food amount"), max_digits=7, decimal_places=2)
#     total_calories = models.DecimalField(_("Total Calories"), max_digits=5, decimal_places=2)
# 
#         selected_food_amount DECIMAL NOT NULL,
#         total_calories DECIMAL NOT NULL,
#         total_protein DECIMAL NOT NULL,
#         total_fat DECIMAL NOT NULL,
#         total_carbohydrates DECIMAL NOT NULL,
#         food_name FLOAT NOT NULL,
#         food_weight DECIMAL NOT NULL,
#         food_calories DECIMAL,
#         food_protein DECIMAL,
#         food_fat DECIMAL,
#         food_carbohydrates DECIMAL,
#         dish_name FLOAT,
#         dish_weight DECIMAL,
#         dish_calories DECIMAL,
#         dish_protein DECIMAL,
#         dish_fat DECIMAL,
#         dish_carbohydrates DECIMAL,
#         FOREIGN KEY (user_id) REFERENCES User(id),
#         FOREIGN KEY (food_name) REFERENCES food_product(id),
#         FOREIGN KEY (food_weight) REFERENCES food_product(id),
#         FOREIGN KEY (food_calories) REFERENCES food_product(id),
#         FOREIGN KEY (food_protein) REFERENCES food_product(id),
#         FOREIGN KEY (food_fat) REFERENCES food_product(id),
#         FOREIGN KEY (food_carbohydrates) REFERENCES food_product(id),
#         FOREIGN KEY (dish_name) REFERENCES dish_with_recipe(id),
#         FOREIGN KEY (dish_weight) REFERENCES dish_with_recipe(id),
#         FOREIGN KEY (dish_calories) REFERENCES dish_with_recipe(id),
#         FOREIGN KEY (dish_protein) REFERENCES dish_with_recipe(id),
#         FOREIGN KEY (dish_fat) REFERENCES dish_with_recipe(id),
#         FOREIGN KEY (dish_carbohydrates) REFERENCES dish_with_recipe(id)
#     );