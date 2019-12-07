from django.contrib import admin
from .models import Transaction, User
# Register your models here.
from django.contrib.auth.admin import UserAdmin


admin.site.register(User)

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('sender', 'receiver', 'amount', 'currency')
