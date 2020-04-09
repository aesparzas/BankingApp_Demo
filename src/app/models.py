from django.contrib.auth.models import User
from django.db import models


class BaseModel(models.Model):
    created_ts = models.DateTimeField('Created Timestamp', auto_now_add=True)
    updated_ts = models.DateTimeField('Updated Timestamp', auto_now=True)

    class Meta:
        abstract = True

    @classmethod
    def editable_fields(cls):
        return [field.name for field in cls._meta.fields
                if field.editable and field.name != 'id']


class PersonUserModel(models.Model):
    user = models.OneToOneField(User,
                                verbose_name='User',
                                on_delete=models.PROTECT)
    telephone = models.CharField('Telephone',
                                 max_length=16,
                                 blank=True,
                                 null=True)

    class Meta:
        abstract = True

    def full_name(self):
        return '{} {}'.format(self.user.first_name, self.user.last_name)

    def __str__(self):
        return self.full_name()