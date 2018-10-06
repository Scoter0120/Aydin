from django.shortcuts import render
from django.http import HttpResponse
import json
from .models import TD_DATA as td_data


def one(request):
    context = {'data': '这是测试.'}
    return render(request, 'scoter/one.html', context)


def showData(request):
    ret = {}
    if request.is_ajax():
        pageNo = int(request.GET.get("page"))
        rows = int(request.GET.get("rows"))
        end = rows * pageNo
        start = end - rows
        list = td_data.objects.all()[start:end]
        total = list.count()
        datas = []
        for info in list:
            dic = info.__dict__
            dic.pop('_state')
            datas.append(dic)
        ret = {'total': total, 'rows': datas}

        return HttpResponse(json.dumps(ret), content_type='application/json')
