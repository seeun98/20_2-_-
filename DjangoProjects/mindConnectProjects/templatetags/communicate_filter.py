from django import template

register = template.Library()
# 템플릿 필터함수 만들기
#템플릿 필터 : 템플릿 태그에서 | 문자 뒤에 사용하는 필터

@register.filter
def sub(value, arg):
    return value - arg