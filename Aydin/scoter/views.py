from django.shortcuts import render
from django.http import HttpResponse
import json,datetime
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
        list = td_data.objects.all().order_by("-UPDATE_TIME")[start:end]  # 按照UPDATE_TIME倒序
        total = list.count()
        datas = []
        for info in list:
            dic = info.__dict__
            dic.pop('_state')
            datas.append(dic)
        ret = {'total': total, 'rows': datas}

    return HttpResponse(json.dumps(ret), content_type='application/json')


def gather(request):
    if request.is_ajax():
        category = request.GET.get("category", None)
        value = request.GET.get("value", None)
        dataDate = request.GET.get("dataDate", None)
        update_time = datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S')  # 按一定格式获取当前日期时间
        ip = request.META['REMOTE_ADDR']
        td_data.objects.create(
            FACTORY='1100',
            CATEGORY=category,
            VALUE=value,
            DATA_DATE=dataDate,
            UPDATE_TIME=update_time,
            IP_ADDRESS=ip
        )
    return HttpResponse(json.dumps("true"), content_type='application/json')
