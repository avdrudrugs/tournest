# Generated by Django 4.0.1 on 2022-01-15 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tours_kg', '0008_alter_booknow_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booknow',
            name='date',
            field=models.DateTimeField(verbose_name='Дата бронирования'),
        ),
    ]
