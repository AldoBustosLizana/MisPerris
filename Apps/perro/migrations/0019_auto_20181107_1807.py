# Generated by Django 2.0.9 on 2018-11-07 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perro', '0018_auto_20181107_1802'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perro',
            name='fotografia',
            field=models.ImageField(blank=True, null=True, upload_to='perro/images/'),
        ),
    ]
