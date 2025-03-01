from django.contrib import admin
from .models import Complaint, Flat, Owner


class OwnerFlatInline(admin.TabularInline):
    model = Flat.owners.through
    raw_id_fields = ('owner',)
    extra = 0


class FlatAdmin(admin.ModelAdmin):
    inlines = [OwnerFlatInline]
    search_fields = ['town', 'address']
    readonly_fields = ['created_at']
    raw_id_fields = ['liked_by']
    list_filter = [
        'new_building',
        'has_balcony',
        'active',
        'town'
    ]
    list_display = (
        'address',
        'price',
        'new_building',
        'construction_year',
        'town'
    )
    list_display_links = ('address',)
    list_editable = (
        'price',
        'new_building',
        'construction_year',
        'town'
    )
    fields = (
        'owner',
        'owners_phonenumber',
        'owner_pure_phone',
        'new_building',
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
        'liked_by',
    )

admin.site.register(Flat, FlatAdmin)

class OwnerFlatInline(admin.TabularInline):
    model = Flat.owners.through
    raw_id_fields = ('owner',)
    extra = 0


class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ['user', 'flat']
    readonly_fields = ['created_at']
    list_display = ('user', 'flat', 'created_at', 'short_text')
    search_fields = ('text',)
    list_filter = ('created_at',)

    def short_text(self, obj):
        if obj.text:
            return f"{obj.text[:50]}..." if len(obj.text) > 50 else obj.text
        return "Текст отсутствует"

    short_text.short_description = 'Текст жалобы'


admin.site.register(Complaint, ComplaintAdmin)


class OwnerAdmin(admin.ModelAdmin):
    list_display = ('name', 'phonenumber', 'pure_phone', 'get_flats',)
    raw_id_fields = ('flats',)
    search_fields = ['name']
    @admin.display(description='Квартиры в собственности')
    def get_flats(self, obj):
        return ", ".join([flat.address for flat in obj.flats.all()])


admin.site.register(Owner, OwnerAdmin)
