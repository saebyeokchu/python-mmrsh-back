from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from enroll.service.AuthService import AuthService


class Auth : 
    @api_view(['POST'])
    def createUser(request) :
        try :
            username = request.data["username"]
            password = request.data["password"]
            user = AuthService.createUser(username, password)
            if user:
                print(user)
                return Response(user, status=status.HTTP_200_OK)
        except :
            return Response(status = status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    @api_view(['POST'])
    def authUser(request) :
        try :
            username = request.data["username"]
            password = request.data["password"]

            user = AuthService.authUser(username, password)
            return Response(user, status=status.HTTP_200_OK)
        except :
            return Response(status = status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    @api_view(['POST'])
    def getUserByEmail(request) :
        try :
            email = request.POST.get("email")
            user = AuthService.getUserByEmail(email)
            return Response(user, status=status.HTTP_200_OK)
        except :
            return Response(status = status.HTTP_500_INTERNAL_SERVER_ERROR)
        