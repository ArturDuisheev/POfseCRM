from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

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


class EmployeeRegister(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    position = models.IntegerField(choices=POSITION, default=1)
    password = models.CharField(max_length=18)
    email = models.EmailField()
