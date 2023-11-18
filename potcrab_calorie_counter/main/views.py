from django.shortcuts import render, redirect
from .models import Food, FoodCategory, UserWeight, UserCalorieGoal
from .forms import FoodForm, UserWeightForm, UserCalorieGoalForm
from django.core.paginator import Paginator
from django.db.models import Count


def index(request):
    # foods = Food.objects.all().order_by('id')
    foods = Food.objects.all().order_by('id')

    p = Paginator(Food.objects.all(), 2)
    page = request.GET.get('page')
    foods2 = p.get_page(page)

    context = {
        'foods': foods,
        'foods2': foods2,
        }

    return render(request, "main/index.html", context)

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

def show_food(request, food_id):
    food = Food.objects.get(pk=food_id)
    context = {
        'food':food,
    }
    return render(request, "main/show-food.html", context)

def create_dish(request):
    return render(request, "main/create-dish.html")

# def dish_categories(request):
#     return render(request, "main/dish-categories.html")

# def dish_list(request):
#     return render(request, "main/dish-list.html")

def food_categories(request):
    categories = FoodCategory.objects.order_by('id')
    food_in_category_count = Food.objects.annotate(Count("category"))
    context = {
        'categories': categories,
        'food_in_category_count': food_in_category_count,
    }
    return render(request, "main/food-categories.html", context)

def show_food_categories(request, category_id):
    category = FoodCategory.objects.get(pk=category_id)
    context = {
        'category': category,
    }
    return render(request, "main/show-food-categories.html", context)

def food_list(request):
    return render(request, "main/food-list.html")

def login(request):
    return render(request, "registration/login.html")

def logout(request):
    return render(request, "registration/logout.html")

def register(request):
    return render(request, "registration/register.html")

def user_profile(request):
    context = {}
    # Weight
    weight_form = UserWeightForm()
    weight = UserWeight.objects.order_by('-created_at')
    context['weight']=weight
    if request.method == 'POST':
        if 'save' in request.POST:
            pk = request.POST.get('save')
            if not pk:
                weight_form = UserWeightForm(request.POST)
            else:
                weight = UserWeight.objects.get(id=pk)
                weight_form = UserWeightForm(request.POST, instance=weight)
            weight_form.save()
            weight_form = UserWeightForm()
        elif 'delete' in request.POST:
            pk = request.POST.get('delete')
            weight = UserWeight.objects.get(id=pk)
            weight.delete()
        elif 'edit' in request.POST:
            pk = request.POST.get('edit')
            weight = UserWeight.objects.get(id=pk)
            weight_form = UserWeightForm(instance=weight)
    context['weight_form']=weight_form

    # Calorie Goal 
    calorie_goal_form = UserCalorieGoalForm()
    calorie_goal = UserCalorieGoal.objects.order_by('-created_at')
    context['calorie_goal']=calorie_goal
    if request.method == 'POST':
        if 'save' in request.POST:
            calorie_goal_form.save()
            calorie_goal_form = UserCalorieGoalForm()
    context['calorie_goal_form']=calorie_goal_form


    return render(request, "user/user-profile.html", context)

def show_weight(request):
    context = {}
    weight_form = UserWeightForm()
    weight = UserWeight.objects.order_by('-created_at')
    context['weight']=weight
    if request.method == 'POST':
        if 'save' in request.POST:
            pk = request.POST.get('save')
            if not pk:
                weight_form = UserWeightForm(request.POST)
            else:
                weight = UserWeight.objects.get(id=pk)
                weight_form = UserWeightForm(request.POST, instance=weight)
            weight_form.save()
            weight_form = UserWeightForm()
        elif 'delete' in request.POST:
            pk = request.POST.get('delete')
            weight = UserWeight.objects.get(id=pk)
            weight.delete()
        elif 'edit' in request.POST:
            pk = request.POST.get('edit')
            weight = UserWeight.objects.get(id=pk)
            weight_form = UserWeightForm(instance=weight)
    context['weight_form']=weight_form
    return render(request, "user/show-weight.html", context)

def show_calorie_goal(request):
    context = {}
    calorie_goal_form = UserCalorieGoalForm()
    calorie_goal = UserCalorieGoal.objects.latest('-created_at')
    context['calorie_goal']=calorie_goal
    if request.method == 'POST':
        if 'save' in request.POST:
            pk = request.POST.get('save')
            if not pk:
                calorie_goal_form = UserCalorieGoalForm(request.POST)
            else:
                calorie_goal = UserCalorieGoal.objects.get(id=pk)
                calorie_goal_form = UserCalorieGoalForm(request.POST, instance=calorie_goal)
            calorie_goal_form.save()
            calorie_goal_form = UserCalorieGoalForm()
        elif 'delete' in request.POST:
            pk = request.POST.get('delete')
            calorie_goal = UserCalorieGoal.objects.get(id=pk)
            calorie_goal.delete()
        elif 'edit' in request.POST:
            pk = request.POST.get('edit')
            calorie_goal = UserCalorieGoal.objects.get(id=pk)
            calorie_goal_form = UserCalorieGoalForm(instance=calorie_goal)
    context['calorie_goal_form']=calorie_goal_form
    return render(request, "user/show-weight.html", context)