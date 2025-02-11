from django.contrib.auth import authenticate
from django.contrib.auth.models import User

from enroll.serializers import CustomUserSerializer
from enroll.models import CustomUser
from django.contrib.auth.hashers import check_password


class AuthService : 
    def createUser(username, password) :

        user = CustomUser(
            username=username,
            phoneNumber=None,
            age=28,
            reserveId=1,
            paymentType=1,
            paymentAmount=500,
            contractId=1,
            note=None,
         )


        user.set_password(password)  # Hashes the password securely

        user.save()

        serialize = CustomUserSerializer(user)

        return serialize.data
        
    def authUser(username, password) :
        try:
            # Attempt to fetch the user by username
            print("username",username)

            user = CustomUser.objects.get(username=username)
            print("user",user)
            if user and check_password(password, user.password):  # Check hashed password
                serialize = CustomUserSerializer(user)
                return serialize.data
        except CustomUser.DoesNotExist:
            return None
        return None
        
    def getUserByEmail(email):
        try:
            user = CustomUser.objects.get(email=email)
            return user
        except CustomUser.DoesNotExist:
            return None