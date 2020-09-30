from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Article(models.Model): #질문 모델
    title = models.CharField('제목', max_length=126, null=False)
    content = models.TextField('내용', null = False)
    #author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField('작성일', auto_now_add=True)
    modify_date = models.DateTimeField(null=True, blank=True)
    def __str__(self):
        return '[{}] {}'.format(self.id, self.title)
    
    
class Answer(models.Model):
    question = models.ForeignKey(Article, on_delete=models.CASCADE) #받은 질문
    content = models.TextField() #답변 공간
    created_at = models.DateTimeField() #답변 시기
    #author = models.ForeignKey(User, on_delete=models.CASCADE)
    modify_date = models.DateTimeField(null=True, blank=True)