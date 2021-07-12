from typing import Counter
from django.db import models

class customer(models.Model):
    user_id = models.AutoField
    user_name = models.CharField(max_length=50)
    user_mail = models.CharField(max_length=60)
    user_cbal = models.IntegerField()
    start_date = models.DateField()

    def __str__(self):
        return self.user_name

class transfer(models.Model):
    tranfer_id = models.AutoField
    fro_user_id = models.CharField(max_length=50)
    to_user_id = models.CharField(max_length=50)
    amt_transf = models.IntegerField()
    tr_date = models.DateField(auto_now=True)
    tr_time = models.TimeField(auto_now=True)

    def __str__(self):
        return "TR" + str((self.id))

# Create your models here.
