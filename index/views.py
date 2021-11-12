from django.template import loader  # 导入loader方法
from django.shortcuts import render  # 导入render 方法
# from django.http import HttpResponse

# Create your views here.

# 方式一


# def test_html(request):
#     t = loader.get_template('test.html')
#     html = t.render({'name': 'haha'})
#     return HttpResponse(html)

# 方式二


def test_html(request):
    return render(request, 'test.html', {'name': 'koko'})
