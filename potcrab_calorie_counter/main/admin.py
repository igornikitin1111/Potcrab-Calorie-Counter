from django.contrib import admin
from .models import Food, FoodCategory, UserWeight, UserCaloriesGoal, FoodLog

# Register your models here.

admin.site.register(Food)
admin.site.register(FoodCategory)
admin.site.register(FoodLog)

admin.site.register(UserWeight)
admin.site.register(UserCaloriesGoal)