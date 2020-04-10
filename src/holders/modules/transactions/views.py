from django.db.models import Q
from django.urls import reverse
from django.views.generic import DetailView, TemplateView, ListView, CreateView

from app.mixins import AccountHolderRequiredMixin
from holders.models import Transaction


class SummaryView(AccountHolderRequiredMixin, TemplateView):
    template_name = ''


class TransactionList(AccountHolderRequiredMixin, ListView):
    template_name = ''
    paginate_by = 10

    def get_queryset(self):
        current_holder = self.request.user.holder
        return Transaction.objects.filter(Q(holder=current_holder) |
                                          Q(receiver=current_holder))


class TransactionDetail(AccountHolderRequiredMixin, DetailView):
    pk_url_kwarg = 'transaction_pk'
    template_name = ''


class TransactionCreate(AccountHolderRequiredMixin, CreateView):
    template_name = ''

    def get_success_url(self):
        return reverse('holders:transactions:summary', kwargs=self.kwargs)
