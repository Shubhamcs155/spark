from django.contrib import admin
from bank.models import customer,transfer

# Register your models here.
admin.site.register(customer)
admin.site.register(transfer)