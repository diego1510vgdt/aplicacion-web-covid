# Generated by Django 3.2 on 2021-04-13 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0007_auto_20210413_0135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='positivo',
            name='oxi',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='positivo',
            name='temp',
            field=models.FloatField(max_length=50),
        ),
    ]
