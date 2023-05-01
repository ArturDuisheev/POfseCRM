# Generated by Django 4.2 on 2023-04-27 10:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_project', models.CharField(max_length=100, verbose_name='Наименование проекта')),
                ('description_project', models.TextField(verbose_name='Описание проекта')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='Дата обновления статуса')),
                ('status', models.CharField(choices=[('в разработке', 'В разработке'), ('Завершено', 'Завершено')], max_length=100, verbose_name='Статус')),
                ('stars', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')], default=0, verbose_name='Оценки')),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_organization', models.CharField(max_length=100, verbose_name='Наименование организации')),
                ('name_client', models.CharField(max_length=100, verbose_name='ФИО')),
                ('address', models.CharField(max_length=100, verbose_name='Адрес')),
                ('city', models.CharField(max_length=100, verbose_name='Город')),
                ('country', models.CharField(max_length=100, verbose_name='Страна')),
                ('phone', models.CharField(max_length=100, verbose_name='Телефон')),
                ('email', models.CharField(max_length=100, verbose_name='E-mail')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='Дата обновления статуса')),
                ('status', models.CharField(choices=[('В разработке', 'В разработке'), ('Стадия переговоров', 'Стадия переговоров'), ('Завершено', 'Завершено'), ('Отказ', 'Отказ')], max_length=100, verbose_name='Статус')),
                ('project', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.project', verbose_name='Проект')),
            ],
            options={
                'verbose_name': 'Клиент',
                'verbose_name_plural': 'Клиенты',
                'ordering': ['name_client'],
                'unique_together': {('name_client', 'project')},
            },
        ),
    ]
