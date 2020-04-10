from django.contrib import admin

from holders.models import Holder, Transaction


@admin.register(Holder)
class HolderAdmin(admin.ModelAdmin):
    pass


@admin.register(Transaction)
class ResultAdmin(admin.ModelAdmin):
    pass
