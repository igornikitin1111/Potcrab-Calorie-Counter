from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext
from django.utils.translation import gettext_lazy as _
from django.utils import timezone


# Create your models here.


# class User(models.Model):
#     username = models.CharField(_("Username"), max_length=50)
#     email = models.EmailField(_("E-mail"), max_length=254)
#     first_name = models.CharField(_("First name"), max_length=50)
#     last_name = models.CharField(_("Last name"), max_length=50)
#     # gender = 
#     height = models.DecimalField(_("Height (cm)"), max_digits=7, decimal_places=2)
#     weight = models.DecimalField(_("Weight (kg)"), max_digits=7, decimal_places=2)


class UserWeight(models.Model):
    # user = models.ForeignKey(
    #     User, 
    #     verbose_name=_("user"), 
    #     related_name='user',
    #     on_delete=models.CASCADE,
    # )
    created_at = models.DateTimeField(_("created at"), default=timezone.now, db_index=True)
    weight = models.DecimalField(_("weight"), max_digits=5, decimal_places=2)

    class Meta:
        ordering = ('-created_at',)

#class UserWeightGoal(models.Model):
#   pass


class UserCalories(models.Model):
    # user = models.ForeignKey(
    #     User, 
    #     verbose_name=_("user"), 
    #     on_delete=models.CASCADE
    # )
    calories = models.DecimalField(_("Calories"), max_digits=7, decimal_places=2)
    created_at = models.DateTimeField(_("created at"), default=timezone.now, db_index=True)

class UserCaloriesTotal(models.Model):
    # user = models.ForeignKey(
    #     User, 
    #     verbose_name=_("user"), 
    #     on_delete=models.CASCADE
    # )
    calories_total = models.DecimalField(_("Calories"), max_digits=7, decimal_places=2)
    created_at = models.DateTimeField(_("created at"), default=timezone.now, db_index=True)


class UserCalorieGoal(models.Model):
    # user = models.ForeignKey(
    #     User, 
    #     verbose_name=_("user"), 
    #     on_delete=models.CASCADE
    # )
    calorie_goal = models.DecimalField(_("Calorie goal"), max_digits=7, decimal_places=2)
    created_at = models.DateTimeField(_("created at"), default=timezone.now, db_index=True)


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


class FoodLog(models.Model):
    # user = models.ForeignKey(
    #     User, 
    #     verbose_name=_("user"), 
    #     on_delete=models.CASCADE
    # )
    time_of_day = models.CharField(
        _("Time of day"), 
        default="Breakfast", 
        max_length=50
    )
    food = models.ForeignKey(
        Food, 
        verbose_name=_("Food"), 
        related_name='food',
        on_delete=models.CASCADE
    )
    food_amount = models.DecimalField(
        _("Selected food amount"), 
        default="100",
        max_digits=7, 
        decimal_places=2
    )
    total_calories = models.DecimalField(
        _("Total Calories"), 
        max_digits=5, 
        decimal_places=2
    )