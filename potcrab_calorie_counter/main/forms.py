from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Food


class FoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = [
            'name', 'category', 'portion_weight', 
            'calories', 'protein', 'fat', 
            'carbohydrates', 'recipe', 'food_image',
            ]
        recipe_placeholder = """For 1 kg of lasagna you need:
1 pound sweet Italian sausage
3/4 pound lean ground beef
..."""
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Apple',
            }),
            'portion_weight': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '100 g',
            }),
            'calories': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'protein': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'fat': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'carbohydrates': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'recipe': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': recipe_placeholder,
            }),
        }