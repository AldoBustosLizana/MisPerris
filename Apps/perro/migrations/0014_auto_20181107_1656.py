# Generated by Django 2.0.9 on 2018-11-07 19:56

import Apps.perro.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perro', '0013_auto_20181107_1650'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perro',
            name='fotografia',
            field=models.ImageField(blank=True, null=True),
        ),
    ]