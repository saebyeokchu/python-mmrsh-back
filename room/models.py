from django.utils.timezone import now
from django.db import models

# Create your models here.
class price(models.Model) :
    roomType = models.IntegerField()
    weekPrice = models.IntegerField()
    monthPrice = models.IntegerField()
    weekDeposit = models.IntegerField()
    monthDeposit = models.IntegerField()
    lastModifiedAt = models.DateTimeField(default=now)

class reserve(models.Model) :
    roomType = models.IntegerField()
    priceType = models.IntegerField()
    price = models.IntegerField()
    deposit = models.IntegerField()
    startDate = models.DateField(default=now)
    endDate = models.DateField(default=now)
    approved = models.BooleanField(default=False)
    lastModifiedAt = models.DateTimeField(default=now)