from django.shortcuts import render


def one(request):
    context = {'data': '这是测试.'}
    return render(request, 'scoter/one.html', context)
