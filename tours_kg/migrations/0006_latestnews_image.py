# Generated by Django 4.0.1 on 2022-01-15 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tours_kg', '0005_alter_booknow_sightseeing'),
    ]

    operations = [
        migrations.AddField(
            model_name='latestnews',
            name='image',
            field=models.ImageField(default=11, upload_to='static/images', verbose_name='Изображение'),
            preserve_default=False,
        ),
    ]
