# Generated by Django 2.0.9 on 2018-11-06 04:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('adopcion', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='persona',
            name='rut',
            field=models.CharField(default=django.utils.timezone.now, max_length=10),
            preserve_default=False,
        ),
    ]