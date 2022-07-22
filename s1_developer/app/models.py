# from tkinter import CASCADE
# import uuid
from django.db import models
from datetime import date

# Create your models here.


class Sales(models.Model):
    # id = id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)
    sales_name = models.CharField(max_length=100)


class Project(models.Model):
    project_code = models.CharField(primary_key=True, max_length=15)
    project_name = models.CharField(max_length=100)


class Reserve(models.Model):
    # id = id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)
    amount = models.CharField(null=True, max_length=10)
    customer_name = models.CharField(max_length=100)
    description = models.TextField()
    project_code = models.ForeignKey(to=Project, on_delete=models.CASCADE)
    request_date = models.DateField(null=True, default=date.today())
    reservation_number = models.CharField(null=True, max_length=100)
    sales = models.ForeignKey(null=True, to=Sales, on_delete=models.CASCADE)
    transaction_date = models.DateField(null=True, default=date.today())
    unit_code = models.CharField(null=True, max_length=100)
    va_code = models.CharField(null=True, max_length=100)
