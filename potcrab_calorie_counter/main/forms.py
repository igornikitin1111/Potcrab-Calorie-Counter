from .models import Food
from django.forms import ModelForm


class FoodForm(ModelForm):
    
    class Meta:
        model = Food
        fields = [
            'name', 
            'category', 
            'portion_weight', 
            'calories', 
            'protein', 
            'fat', 
            'carbohydrates', 
            'recipe'
            ]