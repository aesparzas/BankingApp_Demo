from decimal import Decimal

from django.core.validators import MinValueValidator
from django.db import models
from django.db.models import Sum, Q

from app.models import PersonUserModel, BaseModel


class Holder(BaseModel, PersonUserModel):
    account = models.CharField('Account number',
                               unique=True,
                               primary_key=True,
                               editable=False,
                               max_length=8)
    balance = models.DecimalField('Balance',
                                  max_digits=16,
                                  decimal_places=2,
                                  editable=False,
                                  default=0)

    def calculate_balance(self):
        self.balance = self.transactions_received - self.transactions_made
        self.save()

    def transaction_count(self):
        return (self.transactions_received.count() +
                self.transactions_made.count())

    def create_account_number(self):
        import random
        import string
        return ''.join(random.choices(string.digits, k=8))

    def incomes(self):
        return self.transactions_received\
            .aggregate(Sum('amount'))['amount__sum']

    def outcomes(self):
        return self.transactions_received\
            .aggregate(Sum('amount'))['amount__sum']

    def save(self, *args, **kwargs):
        if not self.account:
            self.account = self.create_account_number()
        super().save()

    @property
    def transactions(self):
        return Transaction.objects.filter(Q(holder=self) |
                                          Q(receiver=self))


class Transaction(BaseModel):

    class Meta:
        ordering = ['-created_ts']

    no_negatives = MinValueValidator(Decimal('0.01'))

    holder = models.ForeignKey(Holder,
                               verbose_name='Accuont Holder',
                               on_delete=models.PROTECT,
                               editable=False,
                               related_name='transactions_made',
                               null=True)
    amount = models.DecimalField('Amount',
                                 max_digits=16,
                                 decimal_places=2,
                                 validators=[no_negatives])
    receiver = models.ForeignKey(Holder,
                                 verbose_name='Accuont Holder',
                                 on_delete=models.PROTECT,
                                 related_name='transactions_received',
                                 null=True)
    description = models.CharField('Description',
                                   max_length=40)

    @property
    def can_be_made(self):
        if self.holder:
            return self.holder.balance >= self.amount
        return True
