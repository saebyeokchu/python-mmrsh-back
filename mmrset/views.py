from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from mmrset.service.QnaService import QnaService

# Create your views here.
class Qna : 
    @api_view(['GET'])
    def getAll(request) :
        try :
            view = request.GET.get("view")
            if view :
                return_data = QnaService.getAll(view)
                return Response(return_data, status=status.HTTP_200_OK)
        except :
                return Response(status = status.HTTP_500_INTERNAL_SERVER_ERROR)

    @api_view(['GET'])
    def delete(request) :
        try :
                return Response(return_data, status=status.HTTP_200_OK)
        except :
                return Response(status = status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    @api_view(['POST'])
    def upsert(request) :
        try :
                return Response(return_data, status=status.HTTP_200_OK)
        except :
                return Response(status = status.HTTP_500_INTERNAL_SERVER_ERROR)