from django.shortcuts import render, get_object_or_404, redirect
from django.db import models
from django.http import HttpResponse
from .models import Article, Answer
from django.contrib import messages
from django.utils import timezone
from .forms import ArticleForm
from django.core.paginator import Paginator

# Create your views here.


#목록 조회
def index(request):
    #article 목록 출력
    article_list = Article.objects.order_by('-created_at')
    context = {'article_list':article_list }

    #입력 파라미터
    page = request.GET.get('page', '1') #get 방식으로 요청한 url에서 page의 값을 가져올 때 사용한다.

    #조회
    article_list = Article.objects.order_by('-created_at')

    #페이징처리
    paginator = Paginator(article_list , 10) #페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)

    context = {'article_list' : page_obj}

    return render(request, 'communicate/article_list.html', context)


#detail 함수 추가
def detail(request,article_id):
    article = Article.objects.get(id = article_id)
    context = {'article': article}
    return render(request, 'communicate/article_detail.html', context)

#답변 등록 함수
def answer_create(request, article_id):
    article = get_object_or_404(Article, pk = article_id)

    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.created_at = timezone.now()
            answer.article = article
            answer.save()
            return redirect('pybo:detail', article_id=article.id)
    else:
        form = AnswerForm()
    context = {'article': article, 'form': form}
    return render(request, 'communicate/article_detail.html', context)


    article.answer_set.create(content=request.POST.get('content'), created_at=timezone.now())
    return redirect('communicate:detail', article_id = article_id)
#질문 수정 함수
def article_modify(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    '''if request.user != article.author:
        messages.error(request, '수정권한이 없습니다.')
        return redirect('communicate:detail', article_id = article_id)
        '''

    if request.method == "POST":
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            article = form.save(commit=False)
            #article.author = request.user
            article.modify_date = timezone.now()
            article.save()
            return redirect('communicate:detail', article_id=article.id)
        else:
            form = ArticleForm(instance=article)
        context = {'form' : form}
        return render(request, 'communicate/article_form.html',context)

#질문 등록 함수
def article_create(request) :
    if request.method == 'POST':  #목록조회 화면에서 질문 등록하기 버튼 -> ~question/create/ 페이지가 GET 방식으로 호출
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.created_at = timezone.now()
            article.save()
            return redirect('communicate:index')
    else:
        form = ArticleForm()
    context = {'form': form}
    return render(request, 'communicate/article_form.html', context)

#@login_required(login_url='common:login')
def answer_delete(request, answer_id):
    answer = get_object_or_404(Answer, pk=answer_id)
    if request.user != answer.author:
        message.error(request, '삭제권한이 없습니다')
    else:
        answer.delete()
    return redirect('communicate:detail', article_id=answer.article.id)