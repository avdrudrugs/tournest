from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

User = get_user_model()


class Region(models.Model):
    reg_name = models.CharField(max_length=30)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.reg_name

    def get_absolute_url(self):
        return reverse('region_detail', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Область'
        verbose_name_plural = 'Область'


class Sight(models.Model):
    class StatusEnum(models.TextChoices):
        USD = "$", "Доллар"
        SOM = "C", "Сом"
        EUR = "€", "Евро"

    sight_name = models.CharField(max_length=50, verbose_name='Достопримечательность')
    province = models.ForeignKey(Region, max_length=40, on_delete=models.CASCADE, verbose_name='Место расположения')
    description = models.TextField(verbose_name='Описание')
    price = models.IntegerField(default=0, verbose_name='Цена')
    duration_days = models.PositiveIntegerField(default=0, verbose_name='Длительность')
    slug = models.SlugField(unique=True)
    image = models.ImageField("изображение")
    currency_type = models.CharField("Тип валюты", choices=StatusEnum.choices, default=StatusEnum.SOM)

    def __str__(self):
        return self.sight_name

    def get_absolute_url(self):
        return reverse('province_detail', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Достопримечательность'
        verbose_name_plural = 'Достопримечательности'


class BookNow(models.Model):
    name = models.CharField(max_length=30, verbose_name='Ваше имя')
    surname = models.CharField(max_length=30, verbose_name='Ваша фамилия')
    phone = models.CharField(max_length=15, verbose_name='Ваш номер телефона')
    email = models.EmailField(verbose_name='Ваша почта')
    sightseeing = models.ForeignKey(Sight, verbose_name='Тур', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0, verbose_name='Количество забронированых туров')
    date = models.DateField(verbose_name='Дата бронирования')

    class Meta:
        verbose_name = 'Бронь'
        verbose_name_plural = 'Брони'


class JoinUs(models.Model):
    email = models.EmailField(verbose_name='Введите вашу почту')

    class Meta:
        verbose_name = 'Подписанные на рассылку'
        verbose_name_plural = 'Подписанные на рассылку'


class Review(models.Model):
    name = models.CharField(max_length=30, verbose_name='Имя пользователя')
    reviews = models.TextField(verbose_name='Отзыв')
    sight = models.ForeignKey(Sight, verbose_name="Достопримечательность", on_delete=models.CASCADE)
    rating = models.PositiveIntegerField("Оценка")

    class Meta:
        verbose_name = 'Отзывы'
        verbose_name_plural = 'Отзыв'

    def __str__(self):
        return self.name


class Image(models.Model):
    image = models.ImageField("Изображения для Меню")

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'
