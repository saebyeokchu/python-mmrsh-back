from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Add custom fields here
    # phone_number = models.CharField(max_length=15, blank=True, null=True)
    phoneNumber = models.CharField(max_length=14, blank=True, null=True)
    age = models.IntegerField()
    reserveId = models.IntegerField()
    paymentType = models.IntegerField()
    paymentAmount = models.IntegerField()
    contractId = models.IntegerField(null=True)
    note = models.TextField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)


# Create your models here.
# class user(models.Model) :
#     name = models.CharField(max_length=10)
#     phoneNumber = models.CharField(max_length=14)
#     age = models.IntegerField()
#     reserveId = models.IntegerField()
#     paymentType = models.IntegerField(max_length=1)
#     paymentAmount = models.IntegerField()
#     note = models.TextField()

