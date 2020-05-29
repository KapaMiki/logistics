from django.contrib import admin
from .models import Order, Equipment



admin.site.site_header = 'Express Logistics Corp'


class EquipmentInLine(admin.TabularInline):
    model = Equipment
    extra = 1
    # readonly_fields = (
    #     'name',
    #     'width',
    #     'leght',
    #     'height',
    #     'weight'
    # )


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = (EquipmentInLine,)

    readonly_fields = (
        'truck',
        'price',
        'status'
    )


    list_display = (
        'first_name',
        'last_name',
        'middle_name',
        'departure',
        'arrival',
        'price',
        'truck',
        'status'
    )

    fieldsets = (
        (
            'Данные заказчика',
            {
                'fields': (
                    'first_name',
                    'last_name',
                    'middle_name',
                    'email',
                    'phone',
                )
            }
        ),
        (
            'Данные доставки',
            {
                'fields': (
                    'price',
                    'status',
                    'departure',
                    'arrival',
                    'truck'
                )
            }
        )
    )

    def truck(self, obj):
        truck = None
        if obj.truck_set.filter():
            truck = obj.truck_set.first()
        return truck
