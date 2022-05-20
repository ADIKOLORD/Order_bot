from django.db import models


class Order(models.Model):
    name = models.CharField(max_length=200, verbose_name='Имя')
    phone_number = models.CharField(max_length=50, default='+996', verbose_name='Номер Телефона')
    porter = models.BooleanField(verbose_name='Портер')
    movers = models.BooleanField(verbose_name='Грузчики')
    furniture_assembly = models.BooleanField(verbose_name='Разборка/сборка мебели')
    garbage_removal = models.BooleanField(verbose_name='Вызов мусора')
    description = models.TextField(blank=True, verbose_name='Описание(Необязательное поле)')

    def __str__(self):
        return self.name
