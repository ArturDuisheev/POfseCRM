from django.utils import timezone

from django.contrib.sites import requests
from django.db import models


class TimeStampedModel(models.Model):
    """
    Модель абстрактного базового класса, обеспечивающая самообновление создаваемых и обновляемых полей.
    """
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.date_updated = timezone.now()
        super(TimeStampedModel, self).save(*args, **kwargs)

    class Meta:
        abstract = True


class Project(TimeStampedModel):
    """
   Представляет проект.
    """
    name_project = models.CharField(max_length=100, verbose_name="Наименование проекта")
    description = models.TextField(verbose_name="Описание проекта")
    status = models.CharField(max_length=100, choices=(
        ("Стадия переговоров", "Стадия переговоров"),
        ('в разработке', 'В разработке'),
        ('Завершено', 'Завершено')
    ), verbose_name="Статус")
    currency_tuple = (
        ('USD', 'USD'),
        ('EUR', 'EUR'),
        ('RUB', 'RUB'),
        ('KGS', 'KGS'),
    )
    currency = models.CharField(max_length=3, choices=currency_tuple, verbose_name="Валюта")
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Сумма")
    stars = models.IntegerField(default=0, choices=[(i, str(i)) for i in range(1, 11)], verbose_name="Оценки")

    def convert_to_som(amount):
        api_key = 'https://openexchangerates.org/api/latest.json?app_id=889c94c4a270499ca3c5cdd9f71e4d8b&base=GBP' \
                  '&callback=someCallbackFunctionа'
        url = 'https://openexchangerates.org/api/latest.json?app_id=889c94c4a270499ca3c5cdd9f71e4d8b' + api_key
        response = requests.get(url)
        if response.status_code == 200:
            rates = response.json()['rates']
            usd_to_som_rate = rates.get('KGS', 1) / rates.get('USD', 1)
            return round(amount * usd_to_som_rate, 2)
        else:
            return None

    def converted_amount(self):
        if self.currency == 'USD':
            return self.convert_to_som(self.amount)
        else:
            return self.amount

    def __str__(self):
        return self.name_project

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'
        ordering = ['name_project']
        unique_together = ('name_project', 'date_created')

    class Meta:
        verbose_name = 'Наименование проекта'
        verbose_name_plural = 'Наименование проектов'

    def __str__(self):
        return self.name_project


class Client(TimeStampedModel):
    """
   Представляет клиента проекта
    """
    name_organization = models.CharField(max_length=100, verbose_name="Наименование организации")
    name_client = models.CharField(max_length=100, verbose_name="ФИО")
    project = models.ForeignKey(Project, verbose_name="Проект", on_delete=models.CASCADE, null=True, blank=True)
    address = models.CharField(max_length=100, verbose_name="Адрес")
    city = models.CharField(max_length=100, verbose_name="Город")
    country = models.CharField(max_length=100, verbose_name="Страна")
    phone = models.CharField(max_length=100, verbose_name="Телефон")
    email = models.CharField(max_length=100, verbose_name="E-mail")
    status = models.CharField(max_length=100, choices=(
        ('В разработке', 'В разработке'),
        ('Стадия переговоров', 'Стадия переговоров'),
        ('Завершено', 'Завершено'),
        ('Отказ', 'Отказ')
    ), verbose_name="Статус")

    def __str__(self):
        return self.name_client

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

        ordering = ['name_client']
        unique_together = ('name_client', 'project')
