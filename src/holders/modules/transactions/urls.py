from django.urls import path

from holders.modules.transactions.views import SummaryView, TransactionList, \
    TransactionCreate

app_name = 'transactions'

urlpatterns = [
    path('', SummaryView.as_view(), name='summary'),
    path('list/', TransactionList.as_view(), name='list'),
    path('transfer/', TransactionCreate.as_view(), name='create'),
]