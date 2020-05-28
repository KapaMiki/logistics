from django.db import models
from apps.locations.models import City
from django.core.exceptions import ValidationError




STATUS = [
    (0, ('В ожидании загрузки')),
    (1, ('В ожидании заполнения')),
    (3, ('В пути')),
]



class Truck(models.Model):
    location = models.ForeignKey(
        City,
        on_delete=models.PROTECT,
        verbose_name='Местоположение',
        related_name='trucks'
    )
    endpoint = models.ForeignKey(
        City,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        default=None,
        related_name='arrive_trucks',
        verbose_name='Конечная точка'
    )
    status = models.IntegerField(
        choices=STATUS,
        default=0,
        verbose_name='Статус'
    )
    remaining_volume = models.FloatField(
        default=84.5,
        verbose_name='Оставшееся объем'
    )
    arrival_date = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name='Дата приезда'
    )
    departure_date = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name='Дата отправки'
    )

    def __str__(self):
        return f'ID грузавика: {self.id}. Местоположение: {self.location.name}. Путь до: {self.endpoint}'

    def clean(self):
        if 84.5 < self.remaining_volume:
            raise ValidationError('Обьем грузовика не может быть больше 84.5')
        if self.remaining_volume < 0:
            raise ValidationError('Обьем грузовика не может быть меньше 0')

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Грузовик'
        verbose_name_plural = 'Грузовики'

            