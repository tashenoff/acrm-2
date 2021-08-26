from django.db import models
from ckeditor.fields import RichTextField
# import readtime 
# Create your models here.

WORDS_PER_MINUTE = 100

class Article(models.Model):
    author = models.ForeignKey("auth.User",on_delete = models.CASCADE,verbose_name = "Автор ")
    title = models.CharField(max_length = 50,verbose_name = "Заголовок")
    content = RichTextField()
    created_date = models.DateTimeField(auto_now_add=True,verbose_name="Дата публикации")
    article_image = models.FileField(blank = True,null = True,verbose_name="Загрузка фото")
    slug = models.SlugField(unique=True, max_length=100)
    rubric = models.ForeignKey('Rubric', null=True, on_delete=models.PROTECT, verbose_name='Рубрика')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super(Article, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-created_date']
        verbose_name = "Статья"
        verbose_name_plural = "Статьи" 


class Rubric (models.Model) :
    name = models.CharField (max_length=20, db_index=True, verbose_name='Название')
    
    def __str__(self):
        return self.name
   
    class Meta:
        verbose_name_plural = 'Рубрики'
        verbose_name = 'Рубрика'
        ordering = ['name']

