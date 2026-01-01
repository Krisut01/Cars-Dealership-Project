from django.contrib import admin
from .models import Dealer, CarMake, CarModel

@admin.register(Dealer)
class DealerAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'state', 'phone')
    list_filter = ('state', 'city')
    search_fields = ('name', 'city', 'state')

@admin.register(CarMake)
class CarMakeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(CarModel)
class CarModelAdmin(admin.ModelAdmin):
    list_display = ('make', 'name')
    list_filter = ('make',)
    search_fields = ('name', 'make__name')
