from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView

from app.mixins import AccountHolderRequiredMixin
from holders.forms import HolderCreateForm


class IndexView(TemplateView):
    template_name = 'index.html'


class AccountView(AccountHolderRequiredMixin, TemplateView):
    template_name = 'account.html'


class RegisterView(CreateView):
    template_name = 'form_base.html'
    form_class = HolderCreateForm
    success_url = reverse_lazy('login')
