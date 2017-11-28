from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    number = models.CharField(max_length=255, verbose_name='ИНН', default='')
    wallet = models.DecimalField(verbose_name="Счет", max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return self.username

