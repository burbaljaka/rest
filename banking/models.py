from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from .managers import UserManager
from django.conf import settings


class User(AbstractUser):

    CURRENCY_CHOICES = (
        ('EUR', 'EUR'),
        ('USD', 'USD'),
        ('GPB', 'GPB'),
        ('RUB', 'RUB'),
        ('BTC', 'BTC'),
    )
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES)
    balance = models.DecimalField(decimal_places=2, max_digits=10)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=20)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['currency', 'balance', 'username']


class Transaction(models.Model):
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Sender', on_delete=models.CASCADE, related_name='sender')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    receiver = models.EmailField(verbose_name='Receiver', default=None)
    currency = models.CharField(verbose_name='Currency', max_length=3)
