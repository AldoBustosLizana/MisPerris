# Generated by Django 2.0.9 on 2018-11-07 08:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('perro', '0003_auto_20181107_0400'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perro',
            name='persona',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='adopcion.Persona'),
        ),
    ]