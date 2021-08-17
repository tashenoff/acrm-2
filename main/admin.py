from django.contrib import admin
from .models import Main, MainService
from customer.models import Customer

@admin.register(Main)
class MainAdmin(admin.ModelAdmin):
    list_display = ('сustomer', 'comment', 'status', 'main_service', 'rec_created',)
    list_filter = ('status',)
 


@admin.register(MainService)
class MainAdmin(admin.ModelAdmin):
    list_display = ('main_service_name',)
    ordering = ('main_service_name',)
    search_fields = ('main_service_name',)



admin.site.site_title = 'Acrm'  
admin.site.site_header = 'Acrm'  