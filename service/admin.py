from django.contrib import admin

from service.models import MainService

@admin.register(MainService)
class MainServiceAdmin(admin.ModelAdmin):
    list_display = ['main_service_name']
    ordering = ('main_service_name',)
    # search_fields = ('main_service_name',)
    # prepopulated_fields = {'slug': ('main_service_name',)}


