# Generated by Django 5.0.4 on 2024-05-04 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_transactioningredient_ingredient_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transactioningredient',
            name='date',
            field=models.DateField(verbose_name='date bought'),
        ),
    ]