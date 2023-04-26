from django.db import models


class Project(models.Model):
    name_project = models.CharField(max_length=100, verbose_name="Наименование проекта")
    description_project = models.TextField(verbose_name="Описание проекта")
    date_created = models.DateTimeField(auto_now_add=True, verbose_name="Дата добавления")
    date_updated = models.DateTimeField(auto_now=True, verbose_name="Дата обновления статуса")

    STATUS_CHOICES = (
        (1, 'В разработке'),
        (2, 'Завершено')
    )

    status = models.CharField(max_length=100, choices=STATUS_CHOICES, verbose_name="Статус")

    STARS_CHOICES = [(i, str(i)) for i in range(1, 11)]

    stars = models.IntegerField(default=0, choices=STARS_CHOICES, verbose_name="Оценки")


class Client(models.Model):
    name_organization = models.CharField(max_length=100, verbose_name="Наименование организации")
    name_client = models.CharField(max_length=100, verbose_name="ФИО")
    project = models.ForeignKey(Project, verbose_name="Проект", on_delete=models.CASCADE)
    address = models.CharField(max_length=100, verbose_name="Адрес")
    city = models.CharField(max_length=100, verbose_name="Город")
    country = models.CharField(max_length=100, verbose_name="Страна")
    phone = models.CharField(max_length=100, verbose_name="Телефон")
    email = models.CharField(max_length=100, verbose_name="E-mail")
    date_created = models.DateTimeField(auto_now_add=True, verbose_name="Дата добавления")
    date_updated = models.DateTimeField(auto_now=True, verbose_name="Дата обновления статуса")

    STATUS_CHOICES = (
        (1, 'В разработке'),
        (2, 'Стадия переговоров'),
        (3, 'Завершено'),
        (4, 'Отказ')
    )

    status = models.CharField(max_length=100, choices=STATUS_CHOICES, verbose_name="Статус")

    def __str__(self):
        return self.name_client

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

        ordering = ['name_client']
        unique_together = ('name_client', 'project')
