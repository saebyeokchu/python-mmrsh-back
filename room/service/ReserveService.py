import json
from room.models import price, reserve
from room.serializers import  reserveSerializer


class ReserveService : 
    def getAllReserve(roomType) :
        try : 
            roomType = int(roomType)
            print("roomType : ",roomType)
            if roomType :
                objects = reserve.objects.filter(roomType = roomType)
            else :
                objects = reserve.objects

            serializer = reserveSerializer(objects, many=True)
            print(serializer.data)
            return serializer.data
        except :
            return RuntimeError
    
    def getAllApprovedReserve() :
        try : 
            serializer = reserveSerializer(reserve.objects.filter(approved = True), many=True)
            print(serializer.data)
            return serializer.data
        except :
            return RuntimeError
    
    def createReserveRequest(info) :
        try : 
            request = reserve(
                roomType = info["roomType"],
                priceType = info["priceType"],
                price = info["price"],
                deposit = info["deposit"],
                startDate = info["startDate"],
                endDate = info["endDate"],
                approved = info["approved"]
            )

            request.save()

            serializer = reserveSerializer(request)
            print(serializer.data)
            return serializer.data
        except :
            return RuntimeError