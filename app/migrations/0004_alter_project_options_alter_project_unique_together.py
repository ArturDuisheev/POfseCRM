# Generated by Django 4.2 on 2023-05-01 13:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_rename_description_project_project_description_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['name_project'], 'verbose_name': 'Проект', 'verbose_name_plural': 'Проекты'},
        ),
        migrations.AlterUniqueTogether(
            name='project',
            unique_together={('name_project', 'date_created')},
        ),
    ]
