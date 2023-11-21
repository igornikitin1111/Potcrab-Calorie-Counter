# Generated by Django 4.2.7 on 2023-11-21 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0023_alter_foodlog_consumed_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='calories',
            field=models.DecimalField(decimal_places=0, max_digits=7, verbose_name='Calories'),
        ),
        migrations.AlterField(
            model_name='food',
            name='carbohydrates',
            field=models.DecimalField(decimal_places=0, max_digits=7, verbose_name='Carbohydrates'),
        ),
        migrations.AlterField(
            model_name='food',
            name='fat',
            field=models.DecimalField(decimal_places=0, max_digits=7, verbose_name='Fat'),
        ),
        migrations.AlterField(
            model_name='food',
            name='protein',
            field=models.DecimalField(decimal_places=0, max_digits=7, verbose_name='Protein'),
        ),
        migrations.AlterField(
            model_name='foodlog',
            name='consumed_amount',
            field=models.DecimalField(decimal_places=0, default=100, max_digits=7, verbose_name='Portion weight (g)'),
        ),
    ]