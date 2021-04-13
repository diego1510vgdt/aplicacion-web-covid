# Generated by Django 3.2 on 2021-04-13 00:27

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0004_positivo_validar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='positivo',
            name='temp',
            field=models.DecimalField(decimal_places=1, max_digits=3, validators=[django.core.validators.MinValueValidator(25), django.core.validators.MaxValueValidator(50)]),
        ),
    ]
