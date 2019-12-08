from django.urls import path
from .views import TransactionView, ClientListView, TransferView#process_transaction

app_name = 'banking'
urlpatterns = [
    path('my/', TransactionView.as_view()),
    path('clients/', ClientListView.as_view()),
    path('transfer/', TransferView.as_view()),
]