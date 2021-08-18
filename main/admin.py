from django.contrib import admin
from .models import Main
from customer.models import Customer
from service.models import MainService

@admin.register(Main)
class MainAdmin(admin.ModelAdmin):
    list_display = ('сustomer', 'comment', 'status', 'main_service', 'rec_created',)
    list_filter = ('status',)
 


admin.site.site_title = 'Acrm'  
admin.site.site_header = 'Acrm'  