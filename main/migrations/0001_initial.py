# Generated by Django 3.2.6 on 2021-08-15 07:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=50, verbose_name='Имя')),
                ('phone', models.CharField(max_length=50, verbose_name='Телефон')),
                ('email', models.CharField(blank=True, max_length=50, null=True, verbose_name='Email')),
                ('company', models.CharField(blank=True, max_length=50, null=True, verbose_name='Название компании')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата заявки')),
            ],
            options={
                'verbose_name': 'Клиента',
                'verbose_name_plural': 'Клиенты',
            },
        ),
        migrations.CreateModel(
            name='MainService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_service_name', models.CharField(max_length=100, verbose_name='Название услуги')),
                ('main_service_price', models.CharField(max_length=100, verbose_name='Цена')),
                ('main_service_comment', models.TextField(blank=True, max_length=255, null=True, verbose_name='Описание услуги')),
                ('main_service_slug', models.SlugField(unique=True)),
            ],
            options={
                'verbose_name': 'Услуги',
                'verbose_name_plural': 'Услуга',
            },
        ),
        migrations.CreateModel(
            name='OriginCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Источник заяки')),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                'verbose_name': 'Источник заявки',
                'verbose_name_plural': 'Источники заявок',
            },
        ),
        migrations.CreateModel(
            name='Main',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.PositiveSmallIntegerField(blank=True, choices=[(1, 'В обработке'), (2, 'На рассмотрении'), (3, 'Завершен')], default=1, null=True, verbose_name='Статус заявки')),
                ('read', models.BooleanField(default=False, verbose_name='Отметить как прочитанное')),
                ('comment', models.TextField(blank=True, max_length=255, null=True, verbose_name='Дополнительный комментарий')),
                ('rec_created', models.DateTimeField(auto_now_add=True, verbose_name='Дата заявки')),
                ('meeting_date', models.DateField(blank=True, null=True, verbose_name='Дата встречи')),
                ('main_service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='main_service', to='main.mainservice', verbose_name='Услуга')),
                ('origin_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='origin_category', to='main.origincategory', verbose_name='Источник заявки')),
                ('сustomer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customer', to='main.customer', verbose_name='Клиент')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
            },
        ),
    ]