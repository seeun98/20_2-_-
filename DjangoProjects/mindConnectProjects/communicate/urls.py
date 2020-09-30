from . import views
from django.contrib import admin
from django.urls import path

app_name = 'communicate' #app_name을 추가해줘서 이 url이 어떤 앱의 url인지 namespace를 등록해주는 부분

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:article_id>/', views.detail, name='detail'), #상세조회
    path('answer/create/<int:article_id>/', views.answer_create, name='answer_create'),
    #/path('article/modify/<int:article_id>/', views.article_modify, name='qrticle_modify'),

]