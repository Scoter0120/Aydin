#!coding:utf-8 
# !@Time   : 2018/10/5 19:44
# !@Author : Aydin
# !@File   : views.py

from django.shortcuts import render


def index(request):
    context = {'title': 'My first app', 'data': '这是我第一个Python3 Web.'}
    return render(request, 'index.html', context)
