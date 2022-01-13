from django.db import models
from django.urls import reverse


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
    sight_name = models.CharField(max_length=50, verbose_name='Достопримечательность')
    province = models.ForeignKey(Region, max_length=40, on_delete=models.CASCADE, verbose_name='Место расположения')
    description = models.TextField(verbose_name='Описание')
    price = models.IntegerField(default=0, verbose_name='Цена')
    duration = models.PositiveIntegerField(default=0, verbose_name='Длительность')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.province, self.sight_name

    def get_absolute_url(self):
        return reverse('province_detail', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Достопримечательность'
        verbose_name_plural = 'Достопримечательность'


class BookNow(models.Model):
    name = models.CharField(max_length=30, verbose_name='Ваше имя')
    surname = models.CharField(max_length=30, verbose_name='Ваша фамилия')
    phone = models.CharField(max_length=15, verbose_name='Ваш номер телефона')
    email = models.EmailField(verbose_name='Ваша почта')
    sightseeing = models.ForeignKey(Sight, on_delete=models.CASCADE, verbose_name='Тур')
    quantity = models.PositiveIntegerField(default=1, verbose_name='Количество забронированых туров')
    date = models.DateTimeField(auto_now=False, verbose_name='Дата бронирования')

    class Meta:
        verbose_name = 'Бронирование'
        verbose_name_plural = 'Забронировать'


class Users(models.Model):
    username = models.CharField(max_length=70, verbose_name='Как к вам обращаться?')
    user_phone = models.CharField(max_length=20, verbose_name='Ваш номер телефона')
    orders = models.ManyToManyField(BookNow, verbose_name='Ваши брони', related_name='orders')

    class Meta:
        verbose_name = 'Пользователи'
        verbose_name_plural = 'Пользователи'


class JoinUs(models.Model):
    email = models.EmailField(verbose_name='Введите вашу почту')


class Review(models.Model):
    name = models.CharField(max_length=30, verbose_name='Имя пользователя')
    reviews = models.TextField(verbose_name='Отзыв')

    class Meta:
        verbose_name = 'Отзывы'
        verbose_name_plural = 'Отзыв'


class LatestNews(models.Model):
    news_name = models.CharField(max_length=100, verbose_name='Трендовые Новости')
    text_news = models.TextField(verbose_name='Описание')
    pub_date = models.DateField(verbose_name='Дата добавления')
