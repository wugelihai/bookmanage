from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

# 定义视图函数
def index(request):
    # 参数1：当前请求
    # 参数2：模板文件
    return render(request, 'index.html')
    return HttpResponse('OK')
