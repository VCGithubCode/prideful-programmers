from django.contrib import admin
from .models import Venue, City

admin.site.register(Venue)

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('city_name', 'country')