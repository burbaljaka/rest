from rest_framework import serializers
from .models import Transaction, User
from django.utils import timezone



class TransactionSerializer(serializers.ModelSerializer):
    sender = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())
    class Meta:
        model = Transaction
        fields = ('amount', 'receiver', 'currency', 'date', 'sender')


class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('email', 'username', 'currency')


class TransactionCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Transaction
        fields = ('amount', 'receiver')
