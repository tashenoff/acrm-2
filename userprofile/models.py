from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

#user name
#useremail
#usertype
#phone

class Profile(models.Model):
    user_type = (
        ("owner","Владелец"),
        ("manager","Менеджер"),
    )
    
    user = models.OneToOneField(get_user_model(), verbose_name="Пользователь", on_delete=models.CASCADE)
    user_type = models.CharField(verbose_name="Тип пользователя", max_length=50, blank=True, null=True)
    user_phone = models.CharField(verbose_name="Телефон", max_length=12, blank=True, null=True)
    
    def __str__(self):
        return self.user.username

        
    class Meta:
        verbose_name_plural = 'Профили'
        verbose_name = 'Профиль'
   
    

@receiver(post_save, sender=get_user_model())
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        instance.profile.save()

