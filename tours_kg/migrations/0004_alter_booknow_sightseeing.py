# Generated by Django 4.0.1 on 2022-01-14 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tours_kg', '0003_alter_booknow_sightseeing'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booknow',
            name='sightseeing',
            field=models.CharField(blank=True, choices=[('JR', 'Junior'), ('SR', 'Senior'), ('GR', 'Graduate')], max_length=100, null=True, verbose_name='Тур'),
        ),
    ]