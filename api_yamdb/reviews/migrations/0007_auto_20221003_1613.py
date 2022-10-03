# Generated by Django 2.2.16 on 2022-10-03 13:13

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0006_auto_20220902_1533'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='score',
            field=models.PositiveIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)]),
        ),
    ]