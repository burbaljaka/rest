from .models import Transaction, User
from rest_framework import generics
from .serializers import TransactionSerializer, ClientSerializer
from rest_framework import serializers
from rest_framework.fields import CurrentUserDefault



class TransactionView(generics.ListAPIView):

    serializer_class = TransactionSerializer
    queryset = Transaction.objects.all()


class ClientListView(generics.ListAPIView):
    serializer_class = ClientSerializer
    queryset = User.objects.filter(is_superuser=False)
