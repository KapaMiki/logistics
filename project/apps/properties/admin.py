from django.contrib import admin
from .models import DefaultPrice




@admin.register(DefaultPrice)
class DefaultPriceAdmin(admin.ModelAdmin):
    list_display = (
        'kg',
        'cubic_meter',
        'hundred_km',
    )

    fieldsets = (
        (
            None,
            {
                'fields': ('kg', 'cubic_meter', 'hundred_km',)
            }
        ),
    )