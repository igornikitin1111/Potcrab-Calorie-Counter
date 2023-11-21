from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name="index"),

    path('create-food/', views.create_food, name="create-food"),
    path('food-categories/', views.food_categories, name="food-categories"),
    path('food-log/', views.food_log, name="food-log"),
    path('show-food/<food_id>', views.show_food, name="show-food"),
    path('show-food-categories/<category_id>', views.show_food_categories, name="show-food-categories"),
    path('search-food/', views.search_food, name="search-food"),

    path('login/', views.login_user, name="login"),
    path('logout/', views.logout_user, name="logout"),
    path('register/', views.register_user, name="register"),

    path('user-profile/', views.user_profile, name="user-profile"),
    path('show-weight/', views.show_weight, name='show-weight'),
    path('show-weight-chart/', views.weight_chart, name='show-weight-chart'),
    path('show-calorie-goal/', views.show_calorie_goal, name='show-calorie-goal'),
]