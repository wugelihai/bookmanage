from django.shortcuts import render
from book.models import BookInfo

from django.http import HttpResponse


# Create your views here.

# 定义视图函数


def index(request):
    # request ,template ,context=None
    # 参数1：当前请求
    # 参数2：模板文件
    # 参数3：context传递参数
    # 实现业务逻辑
    # 1.先把所有的书籍查询出来
    # select * from bookinfo
    # 这里我们通过orm查询出来
    books = BookInfo.objects.all()
    # 组织数据
    context = {
        'books':books
    }
    return render(request, 'index.html', context)
    # return HttpResponse('OK')
