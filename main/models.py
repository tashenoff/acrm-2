from django.db import models
# from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from customer.models import Customer
# Create your models here.

# FirstName
# phone
# email
# company
# дата автоматическая
# нужно добавить сигнал, если была добавлена заявка
# default=lambda: OriginCategory.objects.get(id=1),

class Main(models.Model):

    status_choice = (
        (1, 'В обработке'),
        (2, 'На рассмотрении'),
        (3, 'Отменен'),
        (4, 'Завершен'),
        
    )
    status = models.PositiveSmallIntegerField(choices=status_choice,blank=True, null=True, default=status_choice[0][0], verbose_name="Статус заявки" )
    read = models.BooleanField(verbose_name="Отметить как прочитанное", default=False)
    сustomer = models.ForeignKey('customer.Customer', null=True, default=None, on_delete=models.CASCADE, related_name="main_customer", verbose_name="Клиент")
    comment = models.TextField(verbose_name="Дополнительный комментарий", max_length=255, blank=True, null=True)
    rec_created = models.DateTimeField(auto_now_add=True, verbose_name="Дата заявки")
    meeting_date = models.DateField(blank=True, null=True, verbose_name="Дата встречи")
    main_service = models.ForeignKey('MainService', on_delete=models.CASCADE, related_name="main_service", verbose_name="Услуга")

    def __str__(self):
        return self.comment

    class Meta:
        verbose_name_plural = 'Заказы'
        verbose_name = 'Заказ'


        
class MainService(models.Model):
    main_service_name = models.CharField(max_length=100, verbose_name="Название услуги")
    main_service_price = models.CharField(max_length=100, verbose_name="Цена")
    main_service_comment = models.TextField(verbose_name="Описание услуги", max_length=255, blank=True, null=True)
    main_service_slug = models.SlugField(unique=True)
    
    def __str__(self):
        return "%s" % self.main_service_name
    class Meta:
        verbose_name = "Услуги"
        verbose_name_plural = "Услуга"   


