from django.shortcuts import render, get_object_or_404, redirect
from django.db import models
from django.http import HttpResponse
from .models import Article
from django.contrib import messages
from django.utils import timezone
# Create your views here.


#목록 조회
def index(request):
    #article 목록 출력
    article_list = Article.objects.order_by('-created_at')
    context = {'article_list':article_list }
    return render(request, 'communicate/article_list.html', context)


#detail 함수 추가
def detail(request,article_id):
    article = Article.objects.get(id = article_id)
    context = {'article': article}
    return render(request, 'communicate/article_detail.html', context)

#답변 등록 함수
def answer_create(request, article_id):
    article = get_object_or_404(Article, pk = article_id)
    article.answer_set.create(content=request.POST.get('content'), created_at=timezone.now())
    return redirect('communicate:detail', article_id = article_id)
#질문 수정 함수
'''def article_modify(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    if request.user != article.author:
        messages.error(request, '수정권한이 없습니다.')
        return redirect('communicate:detail', article_id = article_id)

    if request.method == "POST":
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.modify_date = timezone.now()
            article.save()
            return redirect('communicate:detail', article_id=article.)
'''