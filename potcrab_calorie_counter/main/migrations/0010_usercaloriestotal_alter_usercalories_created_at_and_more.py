# Generated by Django 4.2.7 on 2023-11-19 11:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_alter_userweight_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserCaloriesTotal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calories_total', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Calories')),
                ('created_at', models.DateTimeField(db_index=True, default=django.utils.timezone.now, verbose_name='created at')),
            ],
        ),
        migrations.AlterField(
            model_name='usercalories',
            name='created_at',
            field=models.DateTimeField(db_index=True, default=django.utils.timezone.now, verbose_name='created at'),
        ),
        migrations.AlterField(
            model_name='userweight',
            name='created_at',
            field=models.DateTimeField(db_index=True, default=django.utils.timezone.now, verbose_name='created at'),
        ),
    ]