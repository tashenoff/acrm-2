from django.contrib import admin
from customer.models import Customer

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('firstName', 'mystatus', 'company', 'origin_category', 'phone', 'email', 'company', 'created', )
    ordering = ('firstName',)
    search_fields = ('firstName',)
    list_filter = ('mystatus',)
