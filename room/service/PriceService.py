import json
from room.models import price
from room.serializers import priceSerializer


class PriceService : 
    def getPrice(roomType) :
        try : 
            serializer = priceSerializer(price.objects.filter(roomType = roomType), many=True)
            print(serializer.data)
            return serializer.data
        except :
            return RuntimeError

    def getPrices() :
        try : 
            serializer = priceSerializer(price.objects, many=True)
            print(serializer.data)
            return serializer.data
        except :
            return RuntimeError