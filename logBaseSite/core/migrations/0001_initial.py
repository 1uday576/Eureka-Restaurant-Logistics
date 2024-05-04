# Generated by Django 5.0.4 on 2024-05-04 17:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('typeCategory', models.CharField(choices=[('Fruit', 'Fruit'), ('Vegetable', 'Vegetabl'), ('Meat', 'Meat'), ('SeaFood', 'Sea Food'), ('Poultery', 'Poultery')], max_length=50)),
                ('stock', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Meals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('ingredientList', models.JSONField()),
                ('typeCategory', models.CharField(choices=[('Beverages', 'Beverages'), ('Sandwiches', 'Sandwiches'), ('Burger', 'Burger'), ('Soups', 'Soups'), ('MainEntres', 'Main Entres'), ('Dessert', 'Dessert')], max_length=50)),
                ('cost', models.DecimalField(decimal_places=2, max_digits=2)),
            ],
        ),
        migrations.CreateModel(
            name='TransactionIngredients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(verbose_name='date bought')),
                ('numberSold', models.IntegerField()),
                ('ingredient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.ingredients')),
            ],
        ),
        migrations.CreateModel(
            name='TransactionMeals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(verbose_name='date bought')),
                ('numberSold', models.IntegerField()),
                ('meal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.meals')),
            ],
        ),
    ]
