# Generated by Django 2.0.9 on 2018-11-08 01:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adopcion', '0009_auto_20181107_1900'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='adopcion',
            name='ciudad',
        ),
        migrations.RemoveField(
            model_name='adopcion',
            name='comuna',
        ),
        migrations.RemoveField(
            model_name='adopcion',
            name='dv',
        ),
        migrations.RemoveField(
            model_name='adopcion',
            name='mail',
        ),
    ]
