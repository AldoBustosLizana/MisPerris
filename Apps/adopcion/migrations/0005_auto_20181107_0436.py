# Generated by Django 2.0.9 on 2018-11-07 07:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('adopcion', '0004_auto_20181107_0125'),
    ]

    operations = [
        migrations.AddField(
            model_name='persona',
            name='ciudad',
            field=models.CharField(default=django.utils.timezone.now, max_length=80),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='persona',
            name='comuna',
            field=models.CharField(default=django.utils.timezone.now, max_length=80),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='persona',
            name='telefono',
            field=models.CharField(max_length=9),
        ),
    ]
