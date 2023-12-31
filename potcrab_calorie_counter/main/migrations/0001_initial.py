# Generated by Django 4.2.7 on 2023-11-13 13:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FoodCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='name')),
            ],
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('portion_weight', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Portion weight (g)')),
                ('calories', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Calories')),
                ('protein', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Protein')),
                ('fat', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Fat')),
                ('carbohydrates', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Carbohydrates')),
                ('recipe', models.TextField(verbose_name='Recipe')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.foodcategory', verbose_name='Category')),
            ],
        ),
    ]
