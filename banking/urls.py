from django.urls import path
from .views import TransactionView, ClientListView


app_name = 'banking'
urlpatterns = [
    # path('transfer/',),
    path('my/', TransactionView.as_view()),
    path('clients/', ClientListView.as_view()),
]