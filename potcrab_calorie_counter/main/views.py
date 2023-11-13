from django.shortcuts import render
from .models import Food

def index(request):
    foods = Food.objects.all()
    return render(request, "main/index.html", {'foods': foods})

def about(request):
    return render(request, "main/about-us.html")

def create_food(request):
    return render(request, "main/create-food.html")

def create_dish(request):
    return render(request, "main/create-dish.html")

def dish_categories(request):
    return render(request, "main/dish-categories.html")

def dish_list(request):
    return render(request, "main/dish-list.html")

def food_categories(request):
    return render(request, "main/food-categories.html")

def food_list(request):
    return render(request, "main/food-list.html")

def login(request):
    return render(request, "registration/login.html")

def register(request):
    return render(request, "registration/register.html")