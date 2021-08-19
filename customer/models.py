from django.db import models
from customization.models import OriginCategory

class Customer(models.Model):

    customer_status = (
        (1, 'Новый'),
        (2, 'Постоянный')
        

    )


    mystatus = models.PositiveSmallIntegerField(choices=customer_status,blank=True, null=True, default=customer_status[0][0], verbose_name="тип лида" )
    firstName = models.CharField(verbose_name="Имя", max_length=50, blank=False, null=False)
    phone = models.CharField(verbose_name="Телефон", max_length=50, blank=False, unique=True, error_messages={'unique':"Такой номер уже существует"}, null=False)
    email = models.CharField(verbose_name="Email", max_length=50, blank=True, unique=True, error_messages={'unique':"Такой email уже существует"}, null=True)
    company = models.CharField(verbose_name="Название компании", max_length=50, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Дата регистрации лида")
    origin_category = models.ForeignKey('customization.OriginCategory', null=True, default=customer_status[0][0], on_delete=models.CASCADE, related_name="origin_category", verbose_name="Источник лида")
    
    def __str__(self):
        return "%s" % self.firstName
    class Meta:
        verbose_name = "Клиента"
        verbose_name_plural = "Клиенты"   
    