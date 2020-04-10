from django.views.generic import TemplateView, CreateView

from app.mixins import AccountHolderRequiredMixin
from holders.forms import HolderCreateForm


class IndexView(TemplateView):
    template_name = ''


class AccountView(AccountHolderRequiredMixin, TemplateView):
    template_name = ''


class RegisterView(CreateView):
    template_name = ''
    form_class = HolderCreateForm