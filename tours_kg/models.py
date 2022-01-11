from django.db import models

class Region(models.Model):
    reg_name = models.CharField(max_length=30)

    def __str__(self):
        return self.reg_name


class Sight(models.Model):
    province = models.ForeignKey(Region, max_length=40, on_delete=models.CASCADE)
    description = models.TextField(verbose_name='Описание')
    price = models.IntegerField(default=0)
    duration = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.province


class BookNow(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    phone = models.CharField(max_length=15)
    email = models.EmailField(verbose_name='ИМАИЛ')
    sightseeing = models.ForeignKey(Sight, on_delete=models.CASCADE)






