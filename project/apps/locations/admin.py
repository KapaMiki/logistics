from django.contrib import admin
from .models import City, Distance
from .forms import DistanceForm


admin.site.register(City)

@admin.register(Distance)
class DistanceAdmin(admin.ModelAdmin):
    form = DistanceForm


