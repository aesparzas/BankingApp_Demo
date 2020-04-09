from django.contrib.auth.mixins import UserPassesTestMixin

from holders.models import Holder


class AccountHolderRequiredMixin(UserPassesTestMixin):

    def test_func(self):
        if getattr(self.request.user, 'holder', None):
            if 'account' in self.kwargs:
                try:
                    kwargs_holder = Holder.objects.get(account=
                                                       self.kwargs['account'])
                    return kwargs_holder == self.request.holder
                except:
                    return False
            return True
