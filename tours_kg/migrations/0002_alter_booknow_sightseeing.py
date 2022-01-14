# Generated by Django 4.0.1 on 2022-01-14 11:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tours_kg', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booknow',
            name='sightseeing',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='book_sight', to='tours_kg.sight', verbose_name='Тур'),
        ),
    ]