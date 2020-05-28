from django.db import models
from django.core.exceptions import ValidationError
from apps.locations.models import City, Distance
from apps.properties.models import DefaultPrice
from apps.trucks.models import Truck





default_price = DefaultPrice.objects.first()

STATUS = [
    (0, ('Не оплачено')),
    (1, ('Оплачено')),
]

class Order(models.Model):
    status = models.IntegerField(
        default=0,
        verbose_name='Статус'
    )
    first_name = models.CharField(
        max_length=100,
        verbose_name='Имя'
    )
    last_name = models.CharField(
        max_length=100,
        verbose_name='Фамилия'
    )
    middle_name = models.CharField(
        max_length=100,
        verbose_name='Отчество'
    )
    email = models.EmailField(
        verbose_name='Почта'
    )
    phone = models.CharField(
        max_length=13,
        verbose_name='Телефон'
    )
    truck = models.ForeignKey(
        Truck,
        on_delete=models.PROTECT,
        verbose_name='Грузовик',
        null=True,
        blank=True
    )
    departure = models.ForeignKey(
        City,
        on_delete=models.CASCADE,
        verbose_name='Откуда',
        related_name='departures'
    )
    arrival = models.ForeignKey(
        City,
        on_delete=models.CASCADE,
        verbose_name='Место прибытия'
    )
    arrival_date = models.DateTimeField(
        verbose_name='Дата доставки'
    )

    @property
    def price(self):
        equipents = [equipent for equipent in self.equipments.all()]
        total = 0

        if len(equipents) > 0:
            distance = Distance.objects.filter(cities__in=[self.departure, self.arrival]).first().km
        
            volume_price = 0
            weight_price = 0
            km_price = 0

            for eq in equipents:
                weight_price += eq.weight * default_price.kg
                km_price += distance * (default_price.hundred_km / 100)
            total = (self.get_volume() * default_price.cubic_meter) + weight_price + km_price
        return total
    
    def get_volume(self):
        equipents = [equipent for equipent in self.equipments.all()]
        volume = 0

        if len(equipents) > 0:
            for eq in equipents:
                volume += eq.width * eq.height * eq.length

        return volume
        
    def clean(self):
        if self.get_volume() > 84.5:
            raise ValidationError('Квадратный метр оборудовании больше чем 84.5')

    def save(self, *args, **kwargs):
        self.fill_clean()
        truck = Truck.objects.filter(location=self.departure, remaining_volume__gt=self.get_volume())

        if truck:
            self.truck = truck
        
        return super().save(*args, **kwargs)

    def __str__(self):
        return f'Заказ от {self.first_name}\
                {self.last_name} {self.middle_name}'

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class Equipment(models.Model):
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        verbose_name='Заказ',
        related_name='equipments'
    )
    name = models.CharField(
        max_length=100,
        verbose_name='Название'
    )
    weight = models.FloatField(
        verbose_name='Вес'
    )
    width = models.FloatField(
        verbose_name='Ширина'
    )
    length = models.FloatField(
        verbose_name='Длина'
    )
    height = models.FloatField(
        verbose_name='Высота'
    )
    
    def __str__(self):
        return f'Оборудование {self.name}.\
                 Заказ от {self.order.first_name}\
                 {self.order.last_name} {self.order.middle_name}'

    class Meta:
        verbose_name = 'Оборудование'
        verbose_name_plural = 'Оборудования'

