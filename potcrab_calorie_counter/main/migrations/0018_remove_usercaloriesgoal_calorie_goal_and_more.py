# Generated by Django 4.2.7 on 2023-11-20 15:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0017_alter_foodlog_user_alter_usercalories_user_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usercaloriesgoal',
            name='calorie_goal',
        ),
        migrations.AddField(
            model_name='usercaloriesgoal',
            name='calories',
            field=models.DecimalField(decimal_places=2, max_digits=7, null=True, verbose_name='Calories'),
        ),
        migrations.AlterField(
            model_name='usercaloriesgoal',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='calorie_goals', to=settings.AUTH_USER_MODEL, verbose_name='user'),
        ),
    ]
