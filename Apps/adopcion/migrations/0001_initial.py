# Generated by Django 2.0.9 on 2018-11-06 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellidos', models.CharField(max_length=80)),
                ('fechaNacimiento', models.DateField()),
                ('telefono', models.IntegerField()),
                ('domicilio', models.CharField(max_length=50)),
                ('mail', models.CharField(max_length=100)),
            ],
        ),
    ]
