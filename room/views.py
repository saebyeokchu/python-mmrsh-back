from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from room.service.PriceService import PriceService
from room.service.ReserveService import ReserveService

# Create your views here.
class Price : 
    @api_view(['GET'])
    def getPrice(request) :
        try :
            roomType = request.GET.get("roomType")
            data = PriceService.getPrice(roomType)
            return Response(data, status=status.HTTP_200_OK)
        except :
            return Response(status = status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    @api_view(['GET'])
    def getPrices(request) :
        try :
            data = PriceService.getPrices()
            return Response(data, status=status.HTTP_200_OK)
        except :
            return Response(status = status.HTTP_500_INTERNAL_SERVER_ERROR)
        

class Reserve : 
    @api_view(['GET'])
    def getAllReserve(request) :
        try :
            roomType = request.GET.get("roomType")
            data = ReserveService.getAllReserve(roomType)
            return Response(data, status=status.HTTP_200_OK)
        except :
            return Response(None, status = status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    @api_view(['GET']) 
    def getApprovedReserve(request) :
        try :
            roomType = request.GET.get("roomType")
            data = ReserveService.getAllApprovedReserve(roomType)
            return Response(data, status=status.HTTP_200_OK)
        except :
            return Response(None, status = status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    @api_view(['GET']) 
    def createReserveRequest(request) :
        try :
            info = request.GET.get("info")
            if info :
                data = ReserveService.createReserveRequest(info)
                return Response(data, status=status.HTTP_200_OK)
        except :
            return Response(None, status = status.HTTP_500_INTERNAL_SERVER_ERROR)