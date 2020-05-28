from django.db import models




class City(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name='Название'
    )

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'


class Distance(models.Model):
    cities = models.ManyToManyField(
        City,
    )
    km = models.IntegerField(
        default=0,
        verbose_name='Километр'
    )

    def __str__(self):
        return f'Расстояние между {self.cities}'

    class Meta:
        verbose_name = 'Расстояние'
        verbose_name_plural = 'Расстояния'
