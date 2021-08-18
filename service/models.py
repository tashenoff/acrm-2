from django.db import models


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


