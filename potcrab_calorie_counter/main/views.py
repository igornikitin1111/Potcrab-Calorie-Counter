from django.shortcuts import render, redirect
from .models import Food, FoodCategory
from .forms import FoodForm

def index(request):
    foods = Food.objects.order_by('id')
    return render(request, "main/index.html", {'foods': foods})

def about(request):
    return render(request, "main/about-us.html")

def create_food(request):
    error = ""
    if request.method == 'POST':
        form = FoodForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            error = "Error in filling out form"

    food_categories2 = FoodCategory.objects.order_by('id')
    form = FoodForm()
    context = {
        'food_categories2': food_categories2,
        'form': form,
        'error': error,
    }
    return render(request, "main/create-food.html", context)

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

def logout(request):
    return render(request, "registration/logout.html")

def register(request):
    return render(request, "registration/register.html")

def user_profile(request):
    return render(request, "user/user-profile.html")