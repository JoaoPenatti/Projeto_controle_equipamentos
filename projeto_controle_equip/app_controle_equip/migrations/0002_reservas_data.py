# Generated by Django 5.0.6 on 2024-07-01 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_controle_equip', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservas',
            name='data',
            field=models.DateField(null=True),
        ),
    ]
