from django import forms
from django.db.models import Q
from django.urls import reverse
from django.views.generic import TemplateView, ListView, CreateView

from app.mixins import AccountHolderRequiredMixin
from holders.models import Transaction


class SummaryView(AccountHolderRequiredMixin, TemplateView):
    template_name = 'transactions/summary.html'

    def get_context_data(self, **kwargs):
        transactions = self.request.user.holder.transactions
        context = super().get_context_data(**kwargs)
        context.update({
            'transactions': transactions[:5]
        })
        return context


class TransactionList(AccountHolderRequiredMixin, ListView):
    model = Transaction
    template_name = 'transactions/list.html'
    paginate_by = 10

    def get_queryset(self):
        current_holder = self.request.user.holder
        return Transaction.objects.filter(Q(holder=current_holder) |
                                          Q(receiver=current_holder))


class TransactionCreate(AccountHolderRequiredMixin, CreateView):
    model = Transaction
    fields = Transaction.editable_fields()
    template_name = 'transactions/create.html'

    def form_valid(self, form):
        form.instance.holder = self.request.user.holder
        if not form.instance.can_be_made:
            form.add_error(None, 'not enough balance')
            return super().form_invalid(form)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('holders:transactions:summary', kwargs=self.kwargs)
