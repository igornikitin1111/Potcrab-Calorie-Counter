# Generated by Django 4.2.7 on 2023-11-16 09:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_food_food_image_alter_food_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='food', to='main.foodcategory', verbose_name='Category'),
        ),
    ]
