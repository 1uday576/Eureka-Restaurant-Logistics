# Generated by Django 5.0.4 on 2024-05-04 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_meal_cost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transactioningredient',
            name='ingredient',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='transactionmeal',
            name='meal',
            field=models.CharField(max_length=200),
        ),
    ]
