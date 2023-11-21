from django.shortcuts import render, redirect
from .models import Food, FoodLog, FoodCategory, UserWeight, UserCaloriesGoal
from .forms import FoodForm, UserWeightForm, UserWeightDateForm, UserCaloriesGoalForm, SignUpForm
from django.core.paginator import Paginator
import plotly.express as px
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import F, Sum
from django.utils.timezone import localdate

# Register folder ------->
def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ("You have been logged in!"))
            return redirect('index')
        else:
            messages.success(request, ("There was an error. Please try again..."))
            return redirect('login')
    else:
        return render(request, 'registration/login.html', {})

def logout_user(request):
    logout(request)
    messages.success(
        request, 
        ("You have been logged out. Have a nice day!")
    )
    return redirect("index")

def register_user(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("You have succesfully registered. Welcome to the club, buddy!"))
            return redirect("index")
        else:
            messages.success(request, ("There was a problem registering. Please try again"))
            return redirect("register")
    else:
        return render(request, "registration/register.html", {'form':form})

# Main folder ------->
def index(request):
    foods = Food.objects.all().order_by('id')
    p = Paginator(Food.objects.all(), 3)
    page = request.GET.get('page')
    foods2 = p.get_page(page)
    context = {
        'foods': foods,
        'foods2': foods2,
        }
    return render(request, "main/index.html", context)

def search_food(request):
    if request.method == "POST":
        searched = request.POST['searched']
        food = Food.objects.filter(name__contains=searched)
        context = {"searched": searched, "food": food,}
        return render(request, "main/search-food.html", context)
    else:
        return render(request, "main/search-food.html", {})

@login_required
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
    context = {'food':food,}
    return render(request, "main/show-food.html", context)

def food_categories(request):
    categories = FoodCategory.objects.order_by('id')
    context = {'categories': categories,}
    return render(request, "main/food-categories.html", context)

def show_food_categories(request, category_id):
    category = FoodCategory.objects.get(pk=category_id)
    products = Food.objects.filter(category=category)
    context = {'category':category, 'products': products,}
    return render(request, "main/show-food-categories.html", context)

@login_required
def food_log(request):
    context = {}

    # FoodLog
    today = localdate()
    categories=FoodCategory.objects.all()
    if request.method == 'POST':
        foods = Food.objects.all()
        food = request.POST['food_consumed']
        consumed_amount = request.POST['consumed_amount']
        food_consumed = Food.objects.get(name=food)

        user = request.user
        food_log = FoodLog(
            user=user, 
            food_consumed=food_consumed,
            consumed_date=today,
            consumed_amount=consumed_amount)
        food_log.save()
    else:
        foods = Food.objects.all()

    user_food_log = FoodLog.objects.filter(user=request.user).filter(consumed_date=today)
    
    context['categories']=categories
    context['foods']=foods
    context['user_food_log']=user_food_log
    
    # Total calculations
    total_calories = FoodLog.objects.filter(consumed_date=today).aggregate(sum=Sum('food_consumed__calories'))
    total_protein = FoodLog.objects.filter(consumed_date=today).aggregate(sum=Sum('food_consumed__protein'))
    total_fat = FoodLog.objects.filter(consumed_date=today).aggregate(sum=Sum('food_consumed__fat'))
    total_carbohydrates = FoodLog.objects.filter(consumed_date=today).aggregate(sum=Sum('food_consumed__carbohydrates'))

    context['total_calories']=total_calories
    context['total_protein']=total_protein
    context['total_fat']=total_fat
    context['total_carbohydrates']=total_carbohydrates

    # Calorie goal form
    calorie_goal_form = UserCaloriesGoalForm()
    calories = UserCaloriesGoal.objects.filter(user=request.user).latest('created_at')
    context['calories']=calories
    if request.method == 'POST':
        if 'calorie_goal_save1' in request.POST:
            calorie_goal_form = UserCaloriesGoalForm(request.POST)
            calorie_goal1 = calorie_goal_form.save(commit=False)
            calorie_goal1.user = request.user
            calorie_goal1.save()
            calorie_goal_form = UserCaloriesGoalForm()
            return redirect('food-log')
    context['calorie_goal_form']=calorie_goal_form

    return render(request, "main/food-log.html", context)

@login_required
def food_log_delete(request, product_id):
    food_consumed = FoodLog.objects.filter(id=product_id)

    if request.method == 'POST':
        food_consumed.delete()
        return redirect('food-log')

    context ={}
    return render(request, "main/food-log-delete.html", context)

@login_required
def show_food_log(request):
    context = {}

    categories=FoodCategory.objects.all()
    user_food_log = FoodLog.objects.filter(user=request.user).order_by('-consumed_date')
    
    context['user_food_log']=user_food_log
    context['categories']=categories

    return render(request, "main/show-food-log.html", context)

@login_required
def show_food_log_delete(request, product_id):
    food_consumed = FoodLog.objects.filter(id=product_id)

    if request.method == 'POST':
        food_consumed.delete()
        return redirect('show-food-log')

    context ={}
    return render(request, "main/show-food-log-delete.html", context)

# User folder ------->
@login_required
def user_profile(request):
    context = {}
    # Weight
    weight_form = UserWeightForm()
    weight1 = UserWeight.objects.filter(user=request.user).order_by('-created_at')
    context['weight1']=weight1
    if request.method == 'POST':
        if 'save' in request.POST:
            pk = request.POST.get('save')
            if not pk:
                weight_form = UserWeightForm(request.POST)
            else:
                weight1 = UserWeight.objects.get(id=pk)
                weight_form = UserWeightForm(request.POST, instance=weight1)
            user_profile = weight_form.save(commit=False)
            user_profile.user = request.user
            user_profile.save()
            weight_form = UserWeightForm()
        elif 'delete' in request.POST:
            pk = request.POST.get('delete')
            weight1 = UserWeight.objects.get(id=pk)
            weight1.delete()
        elif 'edit' in request.POST:
            pk = request.POST.get('edit')
            weight1 = UserWeight.objects.get(id=pk)
            weight_form = UserWeightForm(instance=weight1)
    context['weight_form']=weight_form

    # Calorie Goal
    calorie_goal_form = UserCaloriesGoalForm()
    calorie_check = UserCaloriesGoal.objects.filter(user=request.user).all()
    if calorie_check:
        calories = UserCaloriesGoal.objects.filter(user=request.user).latest('created_at')
    else:
        calories = "0"
    context['calories']=calories
    if request.method == 'POST':
        if 'calorie_goal_save' in request.POST:
            calorie_goal_form = UserCaloriesGoalForm(request.POST)
            user_profile = calorie_goal_form.save(commit=False)
            user_profile.user = request.user
            user_profile.save()
            calorie_goal_form = UserCaloriesGoalForm()
            return redirect('user-profile')
    context['calorie_goal_form']=calorie_goal_form

    return render(request, "user/user-profile.html", context)

@login_required
def show_weight(request):
    context = {}
    weight_form = UserWeightForm()
    weight = UserWeight.objects.filter(user=request.user).order_by('-created_at')
    context['weight']=weight
    if request.method == 'POST':
        if 'save' in request.POST:
            pk = request.POST.get('save')
            if not pk:
                weight_form = UserWeightForm(request.POST)
            else:
                weight = UserWeight.objects.get(id=pk)
                weight_form = UserWeightForm(request.POST, instance=weight)
            user_profile = weight_form.save(commit=False)
            user_profile.user = request.user
            user_profile.save()
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

@login_required
def weight_chart(request):
    weight = UserWeight.objects.filter(user=request.user).all()
    start = request.GET.get('start') 
    end = request.GET.get('end')
    if start:
        weight = weight.filter(created_at__gte=start)
    if end:
        weight = weight.filter(created_at__lte=end)
    fig = px.line(
        x=[w.created_at for w in weight], y=[w.weight for w in weight],
        title='Weight chart',
        labels={
            'x': 'Date',
            'y': 'Weight'
        }
    )
    fig.update_layout(title={'font_size': 22, 'xanchor': 'center', 'x': 0.5})
    chart = fig.to_html()
    context = {'chart': chart, 'form': UserWeightDateForm(),}
    return render(request, 'user/show-weight-chart.html', context)

@login_required
def show_calorie_goal(request):
    context = {}
    calorie_goal_form = UserCaloriesGoalForm()
    calorie_check = UserCaloriesGoal.objects.filter(user=request.user).all()
    if calorie_check:
        calorie_goal = UserCaloriesGoal.objects.filter(user=request.user).order_by('-created_at')
    else:
        calorie_goal = "0"
    context['calorie_goal']=calorie_goal
    if request.method == 'POST':
        if 'save' in request.POST:
            calorie_goal_form = UserCaloriesGoalForm(request.POST)
            calorie_goal_form.save()
            calorie_goal_form = UserCaloriesGoalForm()
    context['calorie_goal_form']=calorie_goal_form
    return render(request, "user/show-weight.html", context)