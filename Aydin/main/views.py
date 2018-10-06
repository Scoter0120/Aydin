from django.shortcuts import render
from django.http import HttpResponse
import json


def getData(request):
    param = ''
    if request.is_ajax():
        param = request.GET.get('param') + ",欢迎你"
        #print(param)

    return HttpResponse(json.dumps(param), content_type='application/json')
