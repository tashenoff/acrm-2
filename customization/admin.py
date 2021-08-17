from django.contrib import admin

from customization.models import OriginCategory

@admin.register(OriginCategory)
class OriginCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    ordering = ('name',)
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}

