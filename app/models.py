from django.db import models


class TimeStampedModel(models.Model):
    """
    Модель абстрактного базового класса, обеспечивающая самообновление создаваемых и обновляемых полей.
    """
    date_created = models.DateTimeField(auto_now_add=True)
    # date_updated = models.DateTimeField()

    class Meta:
        abstract = True


class Project(TimeStampedModel):
    """
   Представляет проект.
    """
    name_project = models.CharField(max_length=100, verbose_name="Наименование проекта")
    description = models.TextField(verbose_name="Описание проекта")
    status = models.CharField(max_length=100, choices=(
        ('в разработке', 'В разработке'),
        ('Завершено', 'Завершено')
    ), verbose_name="Статус")
    stars = models.IntegerField(default=0, choices=[(i, str(i)) for i in range(1, 11)], verbose_name="Оценки")

    def __str__(self) -> str:
        return self.name_project

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'
        ordering = 'id name_project'.split()
        unique_together = 'id name_project date_created'.split()


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
    keyword = models.CharField(max_length=100, verbose_name="Ключевое слово", null=True, blank=True)

    def __str__(self) -> str:
        return self.name_client

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

        ordering = ['name_client']
        unique_together = ('name_client', 'project')
