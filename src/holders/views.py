from django.views.generic import TemplateView

from app.mixins import AccountHolderRequiredMixin


class IndexView(TemplateView):
    template_name = ''

class AccountView(AccountHolderRequiredMixin, TemplateView):
    template_name = ''