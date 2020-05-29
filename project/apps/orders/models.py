from django.db import models
from django.core.exceptions import ValidationError
from apps.locations.models import City, Distance
from apps.properties.models import DefaultPrice
from apps.trucks.models import Truck







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
        verbose_name='Имя',
        blank=True,
        null=True
    )
    last_name = models.CharField(
        max_length=100,
        verbose_name='Фамилия',
        blank=True,
        null=True
    )
    middle_name = models.CharField(
        max_length=100,
        verbose_name='Отчество',
        blank=True,
        null=True
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
        verbose_name='Дата доставки',
        null=True,
        blank=True,
    )

    @property
    def price(self):
        default_price = DefaultPrice.objects.first()
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
        # truck = Truck.objects.filter(
        #     location=self.departure, 
        #     remaining_volume__gt=self.get_volume(),
        #     status__in=[0,1]
        # )

        # if truck:
        #     truck = truck.first()
        #     self.truck = truck
        #     truck.status = 1
        #     truck.remaining_volume - self.get_volume()
            
        #     # if truck.remaining_volume < 40:
        #     #     truck.
        # elif Truck.objects.filter(status=0):
        #     truck = Truck.objects.get(status=0)
        #     truck.location = self.departure
        # else:
        #     raise ValidationError('На данный момент нету свободных грузовиков.')
        
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

