from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            'id',
            'username',  # From AbstractUser
            'email',     # From AbstractUser
            'phoneNumber',
            'age',
            'reserveId',
            'paymentType',
            'paymentAmount',
            'contractId',
            'note',
        ]