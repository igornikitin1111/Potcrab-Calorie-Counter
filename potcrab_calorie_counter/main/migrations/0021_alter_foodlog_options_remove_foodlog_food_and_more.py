# Generated by Django 4.2.7 on 2023-11-21 08:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0020_alter_usercaloriesgoal_calories_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='foodlog',
            options={'verbose_name': 'Food Log', 'verbose_name_plural': 'Food Log'},
        ),
        migrations.RemoveField(
            model_name='foodlog',
            name='food',
        ),
        migrations.RemoveField(
            model_name='foodlog',
            name='food_amount',
        ),
        migrations.RemoveField(
            model_name='foodlog',
            name='time_of_day',
        ),
        migrations.RemoveField(
            model_name='foodlog',
            name='total_calories',
        ),
        migrations.AddField(
            model_name='foodlog',
            name='food_consumed',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='food_log_consumed', to='main.food', verbose_name='Food'),
        ),
        migrations.AlterField(
            model_name='foodlog',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='food_log', to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
        migrations.AlterField(
            model_name='usercaloriesgoal',
            name='calories',
            field=models.DecimalField(decimal_places=2, max_digits=7, null=True, verbose_name='Calories'),
        ),
    ]
