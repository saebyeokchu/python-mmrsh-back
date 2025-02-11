from rest_framework import serializers
from room.models import price

class priceSerializer(serializers.ModelSerializer) :
    roomType = serializers.IntegerField()
    weekPrice = serializers.IntegerField()
    monthPrice = serializers.IntegerField()
    weekDeposit = serializers.IntegerField()
    monthDeposit = serializers.IntegerField()
    lastModifiedAt = serializers.DateTimeField()

    class Meta:
        model = price
        fields = ['roomType', 'weekPrice', 'monthPrice', 'weekDeposit', 'monthDeposit', 'lastModifiedAt']

class reserveSerializer(serializers.ModelSerializer) :
    roomType = serializers.IntegerField()
    userId = serializers.IntegerField()
    priceType = serializers.IntegerField()
    price = serializers.IntegerField()
    deposit = serializers.IntegerField()
    startDate = serializers.DateField()
    endDate = serializers.DateField()
    approved = serializers.BooleanField()
    lastModifiedAt = serializers.DateTimeField()

    class Meta:
        model = price
        fields = ['roomType', 'userId', 'priceType', 'price', 'deposit', 'startDate', 'endDate', 'approved','lastModifiedAt']
