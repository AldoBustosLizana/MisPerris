# Generated by Django 2.0.9 on 2018-11-07 22:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perro', '0020_auto_20181107_1827'),
        ('adopcion', '0008_auto_20181107_1846'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Persona',
            new_name='Adopcion',
        ),
    ]
