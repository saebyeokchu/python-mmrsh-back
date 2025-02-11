from rest_framework import serializers
from .models import Qna

class QnaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Qna
        fields = [
            'id',
            'question', 
            'answer',    
            'view',
            'sortOrder',
            'lastModifiedAt'
        ]