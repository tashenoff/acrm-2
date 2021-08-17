# Generated by Django 3.2.6 on 2021-08-17 18:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customization', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mystatus', models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Новый'), (2, 'Постоянный')], default=1, null=True, verbose_name='тип лида')),
                ('firstName', models.CharField(max_length=50, verbose_name='Имя')),
                ('phone', models.CharField(max_length=50, verbose_name='Телефон')),
                ('email', models.CharField(blank=True, max_length=50, null=True, verbose_name='Email')),
                ('company', models.CharField(blank=True, max_length=50, null=True, verbose_name='Название компании')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата заявки')),
                ('origin_category', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='origin_category', to='customization.origincategory', verbose_name='Источник заявки')),
            ],
            options={
                'verbose_name': 'Клиента',
                'verbose_name_plural': 'Клиенты',
            },
        ),
    ]