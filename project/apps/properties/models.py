from django.db import models
from django.core.exceptions import ValidationError







# kg = 500 tg
# 1 metr kub = 500 tg 
# 100 km = 20 000 tg 
# 84.5 obiem gruzavika 


class DefaultPrice(models.Model):
    kg = models.IntegerField(
        default=500,
        verbose_name='Цена за один киллограм'
    )
    cubic_meter = models.IntegerField(
        default=500,
        verbose_name='Цена за один кубический метр'
    )
    hundred_km = models.IntegerField(
        default=20000,
        verbose_name='Цена за каждые 100 киллометров'
    )

    def __str__(self):
        return 'Цены'
    
    def clean(self):
        if not self.pk and DefaultPrice.objects.exists():
            # if you'll not check for self.pk
            # then error will also raised in update of exists model
            raise ValidationError('Вы уже указали цены')

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)
    
    class Meta:
        verbose_name = 'Цены'
        verbose_name_plural = 'Цены'        