from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class User(AbstractUser):

    CURRENCY_CHOICES = (
        ('EUR', 'EUR'),
        ('USD', 'USD'),
        ('GPB', 'GPB'),
        ('RUB', 'RUB'),
        ('BTC', 'BTC'),
    )
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, blank=True)
    balance = models.DecimalField(decimal_places=2, max_digits=10, blank=True, default=0)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=20)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['currency', 'balance', 'username']

    def __str__(self):
        return self.username


class Transaction(models.Model):
    sender = models.ForeignKey(User, verbose_name='Sender', on_delete=models.CASCADE, related_name='sender')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    receiver = models.EmailField(verbose_name='Receiver', default=None)
    currency = models.CharField(verbose_name='Currency', max_length=3, blank=True)
    date = models.DateTimeField(verbose_name='Date', auto_now_add=True)

    def __str__(self):
        return str(self.date)
