from django.urls import path, include

from holders.views import AccountView, IndexView

app_name = 'holders'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('<slug:account>/', AccountView.as_view(), name='account'),
    path('<slug:account>/transactions/',
         include('holders.modules.transactions.urls',
                 namespace='transactions')),
]