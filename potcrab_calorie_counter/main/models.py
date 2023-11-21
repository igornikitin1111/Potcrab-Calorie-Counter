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

    def __str__(self):
        return f'{self.user.username} - {self.weight} - {self.created_at}'


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
    def __str__(self):
        return f'{self.user.username} - {self.calories} - {self.created_at}'

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
    calories = models.DecimalField(_("Calories"), max_digits=7, decimal_places=0)
    protein = models.DecimalField(_("Protein"), max_digits=7, decimal_places=0)
    fat = models.DecimalField(_("Fat"), max_digits=7, decimal_places=0)
    carbohydrates = models.DecimalField(_("Carbohydrates"), max_digits=7, decimal_places=0)
    recipe = models.TextField(_("Recipe"), null=True, blank=True)
    food_image = models.ImageField(null=True, blank=True, upload_to="food/")

    def __str__(self):
        return self.name


class FoodLog(models.Model):
    user = models.ForeignKey(
        User, 
        verbose_name=_("User"),
        related_name="food_log", 
        on_delete=models.CASCADE,
        )
    food_consumed = models.ForeignKey(
        Food,
        verbose_name=_("Food"),
        related_name="food_log_consumed", 
        on_delete=models.CASCADE,
        null=True
        )
    consumed_amount = models.DecimalField(
        _("Portion weight (g)"), 
        max_digits=7, 
        decimal_places=0,
        default=100,
    )
    consumed_date = models.DateField(
        _("created at"), 
        default=timezone.now, 
        db_index=True, 
        null=True
    )

    class Meta:
        verbose_name = 'Food Log'
        verbose_name_plural = 'Food Log'

    def __str__(self):
        return f'{self.user.username} - {self.food_consumed} - {self.consumed_date}'