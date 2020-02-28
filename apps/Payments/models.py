from django.db import models
from ..Bills.models import Bill
from ..Invoices.models import Invoice
from djmoney.models.fields import MoneyField
# Create your models here.


class Payment(models.Model):
    def __str__(self):
        return self.label

    label = models.CharField(max_length=20, unique=True)
    type = models.CharField(max_length=20)
    reference = models.ForeignKey(Bill, on_delete=models.CASCADE)
    balance = MoneyField(max_digits=14, decimal_places=2,
                         default_currency='USD')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
