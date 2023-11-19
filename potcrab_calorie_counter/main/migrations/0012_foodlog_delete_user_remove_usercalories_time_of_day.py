# Generated by Django 4.2.7 on 2023-11-19 16:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_usercalories_time_of_day'),
    ]

    operations = [
        migrations.CreateModel(
            name='FoodLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_of_day', models.CharField(default='Breakfast', max_length=50, verbose_name='Time of day')),
                ('food_amount', models.DecimalField(decimal_places=2, default='100', max_digits=7, verbose_name='Selected food amount')),
                ('total_calories', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Total Calories')),
                ('food', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='food', to='main.food', verbose_name='Food')),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.RemoveField(
            model_name='usercalories',
            name='time_of_day',
        ),
    ]
