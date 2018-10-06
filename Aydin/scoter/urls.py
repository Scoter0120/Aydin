#!coding:utf-8 
#!@Time   : 2018/10/6 20:04
#!@Author : Aydin
#!@File   : urls.py

from django.urls import path
from scoter import views

urlpatterns = [
    path('one', views.one, name='one'),
]