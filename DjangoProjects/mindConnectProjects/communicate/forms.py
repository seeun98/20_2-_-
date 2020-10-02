from django import forms
from communicate.models import Article, Answer

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content']

        labels = {
            'title': '제목',
            'content': '내용',
        }
'''
        widgets = {
            'title' : forms.TextInput(attrs={'class': 'form-control'}),
            'content' : forms.Textarea(attrs={'class':'form-control', 'rows':10}),

        }'''


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
        labels = {
            'content' : '답변내용',
        }