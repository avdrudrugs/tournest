from django.db import models


class Region(models.Model):
    reg_name = models.CharField(max_length=30)

    def __str__(self):
        return self.reg_name


class Sight(models.Model):
    sight_name = models.CharField(max_length=50, verbose_name='Достопримечательность')
    province = models.ForeignKey(Region, max_length=40, on_delete=models.CASCADE, verbose_name='Место расположения')
    description = models.TextField(verbose_name='Описание')
    price = models.IntegerField(default=0, verbose_name='Цена')
    duration = models.PositiveIntegerField(default=0, verbose_name='Длительность')

    def __str__(self):
        return self.province


class BookNow(models.Model):
    name = models.CharField(max_length=30, verbose_name='Ваше имя')
    surname = models.CharField(max_length=30, verbose_name='Ваша фамилия')
    phone = models.CharField(max_length=15, verbose_name='Ваш номер телефона')
    email = models.EmailField(verbose_name='Ваша почта')
    sightseeing = models.ForeignKey(Sight, on_delete=models.CASCADE, verbose_name='Тур')
    quantity = models.PositiveIntegerField(default=1, verbose_name='Количество забронированных туров')
    for_anonymous_user = models.BooleanField(default=False)
