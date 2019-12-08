from .models import Transaction, User
from rest_framework import generics
from .serializers import TransactionSerializer, ClientSerializer, TransactionCreateSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.utils import timezone


class TransactionView(generics.ListAPIView):
    serializer_class = TransactionSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = Transaction.objects.filter(sender_id=user.id)
        return queryset

class ClientListView(generics.ListAPIView):
    serializer_class = ClientSerializer
    queryset = User.objects.filter(is_superuser=False)

class TransferView(generics.CreateAPIView):
    serializer_class = TransactionCreateSerializer

    def post(self, request):
        context = {
            "request": self.request,
        }
        serializer = TransactionSerializer(data=request.data, context=context)
        print(serializer.initial_data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        sender = request.user.id
        amount = data['amount']
        receiver = data['receiver']
        provider = User.objects.get(pk=int(sender))
        currency = provider.currency
        getter = User.objects.filter(email=receiver)
        if len(getter) == 0:
            return Response({'message': 'No such client with {} email'.format(receiver_email)})
        else:
            if provider.balance < amount:
                return Response({'message': 'Not enough balance to perform such operation'})
            else:
                transaction = Transaction(amount=amount, currency=currency, sender=provider,
                                      date=timezone.now(), receiver=getter[0].email)
                transaction.save()
                provider.balance -= amount
                getter[0].balance += amount
                provider.save()
                getter[0].save()

        return Response({'Message': 'Transfer finished'})

