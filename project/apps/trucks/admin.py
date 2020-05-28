from django.contrib import admin
from .models import Truck




@admin.register(Truck)
class TruckAdmin(admin.ModelAdmin):
    list_display = (
        'location',
        'endpoint',
        'status',
        'remaining_volume',
        'arrival_date',
        'departure_date',
    )

    fieldsets = (
        (
            None,
            {
                'fields': ('location', 'endpoint', 'status', 'remaining_volume', 'arrival_date', 'departure_date',)
            }
        ),
    )