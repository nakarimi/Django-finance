from django.db import models
# Create your models here.


class Account(models.Model):
    class Meta:
        db_table = 'account'

    def __str__(self):
        return self.label

    label = models.CharField(max_length=20, unique=True)
    owner = models.CharField(max_length=20)
    balance = models.IntegerField()
    currency = models.CharField(max_length=5)
    desc = models.CharField(max_length=200, blank=True)
    status = models.BooleanField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
