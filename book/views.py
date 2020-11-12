from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

# 定义视图函数
def index(request):
    return HttpResponse('OK')
