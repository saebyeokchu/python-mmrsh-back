from django.db import models
from django.utils.timezone import now

# Create your models here.
class Qna(models.Model) :
    question = models.TextField()
    answer = models.TextField()
    view = models.BooleanField(default=False)
    sortOrder = models.IntegerField()
    lastModifiedAt = models.DateTimeField(default=now)
