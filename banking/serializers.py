from rest_framework import serializers
from .models import Transaction, User



class TransactionSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())
    class Meta:
        model = Transaction
        fields = ('amount', 'receiver', 'currency', 'date', 'user')


class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('email', 'username', 'currency')


