from django.contrib import admin

from .models import Flat

class FlatAdmin(admin.ModelAdmin):
    search_fields = ['town', 'address']
    readonly_fields = ['created_at']
    fields = (
        'owner',
        'owners_phonenumber',
        'price',
        'town',
        'town_district',
        'address',
        'floor',
        'rooms_number',
        'living_area',
        'has_balcony',
        'active',
        'construction_year',
        'created_at',
    )



admin.site.register(Flat, FlatAdmin)
