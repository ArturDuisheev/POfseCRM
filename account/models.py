from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
)
from django.db import models
from account.managers import CustomUserManager

POSITION = [
    (1, 'Back-end Developer'),
    (2, 'Front-end Developer'),
    (3, 'UX/UI Designer'),
    (4, 'Marketing specialist'),
    (5, 'Sales manager'),
    (6, 'HR manager'),
    (7, 'Product manager'),
    (8, 'Project manager'),
    (9, 'CEO, founders'),
    (10, 'others')]


class User(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key=True, unique=True)
    email = models.EmailField(max_length=255, unique=True, verbose_name="Почта")
    position = models.CharField(choices=POSITION, default=10, blank=False, null=False, max_length=10)
    is_active = models.BooleanField(default=True, verbose_name="Активность")
    is_staff = models.BooleanField(default=False, verbose_name="Менеджер")
    is_superuser = models.BooleanField(default=False, verbose_name="Суперпользователь")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email

