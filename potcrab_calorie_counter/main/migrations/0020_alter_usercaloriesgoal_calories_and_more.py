# Generated by Django 4.2.7 on 2023-11-21 07:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_alter_foodlog_time_of_day'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercaloriesgoal',
            name='calories',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True, verbose_name='Calories'),
        ),
        migrations.AlterField(
            model_name='usercaloriesgoal',
            name='created_at',
            field=models.DateTimeField(db_index=True, default=django.utils.timezone.now, null=True, verbose_name='created at'),
        ),
    ]