from django.db import models


class OriginCategory(models.Model):
    name = models.CharField(max_length=100, verbose_name="Источник заяки")
    slug = models.SlugField(unique=True)
    
    def __str__(self):
        return "%s" % self.name
    class Meta:
        verbose_name = "Источник заявки"
        verbose_name_plural = "Источники заявок"   