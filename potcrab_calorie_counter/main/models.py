from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

User = get_user_model()

# Create your models here.


class UserWeight(models.Model):
    user = models.ForeignKey(
        User, 
        verbose_name=_("user"), 
        related_name='weights',
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(_("created at"), default=timezone.now, db_index=True)
    weight = models.DecimalField(_("weight"), max_digits=5, decimal_places=2)

    class Meta:
        ordering = ('-created_at',)


class UserCalories(models.Model):
    user = models.ForeignKey(
        User, 
        verbose_name=_("user"), 
        related_name="calories",
        on_delete=models.CASCADE
    )
    calories = models.DecimalField(_("Calories"), max_digits=7, decimal_places=2)
    created_at = models.DateTimeField(_("created at"), default=timezone.now, db_index=True)


class UserCaloriesTotal(models.Model):
    user = models.ForeignKey(
        User, 
        verbose_name=_("user"), 
        related_name="calories_totals",
        on_delete=models.CASCADE
    )
    calories_total = models.DecimalField(_("Calories"), max_digits=7, decimal_places=2)
    created_at = models.DateTimeField(_("created at"), default=timezone.now, db_index=True)


class UserCaloriesGoal(models.Model):
    user = models.ForeignKey(
        User, 
        verbose_name=_("user"), 
        related_name="calorie_goals",
        on_delete=models.CASCADE
    )
    calories = models.DecimalField(_("Calories"), max_digits=7, decimal_places=2, null=True)
    created_at = models.DateTimeField(_("created at"), default=timezone.now, db_index=True, null=True)


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
        blank=True, null=True
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
    user = models.ForeignKey(
        User, 
        verbose_name=_("user"), 
        related_name="log",
        on_delete=models.CASCADE
    )
    time_of_day = models.CharField(
        _("Time of day"),
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