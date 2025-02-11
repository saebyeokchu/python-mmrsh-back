import json

from mmrset.models import Qna
from mmrset.serializers import QnaSerializer

class QnaService : 
    def getAll(view) :
        try : 
            serializer = QnaSerializer(Qna.objects.filter(view = view), many=True)
            return serializer.data
        except :
            return RuntimeError
        
    def delete(qna_id):
        try:
            qna_entry = Qna.objects.get(id=qna_id)
            qna_entry.delete()
            return {"message": f"QNA entry with ID {qna_id} deleted successfully!"}
        except Qna.DoesNotExist:
            return {"error": f"QNA entry with ID {qna_id} does not exist."}

        except Exception as e:
            return {"error": str(e)}

    
    def upsert(qna) :
        try :        
            id = qna["id"]
         
            if id : # update
                targetQna = Qna.objects.get(id = id)
                targetQna.question = qna["question"]
                targetQna.answer = qna["answer"]
                targetQna.sortOrder = qna["sortOrder"]
                targetQna.save()
            else : #insert
                targetQna = Qna(
                    id = id,
                    question = qna["question"],
                    answer = qna["answer"],
                    sortOrder = qna["sortOrder"],
                )
                targetQna.save()

            serializer = QnaSerializer(targetQna)
            return serializer.data
        except :
            return RuntimeError