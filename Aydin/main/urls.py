#!coding:utf-8 
#!@Time   : 2018/10/5 14:22
#!@Author : Aydin
#!@File   : urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('getData', views.getData, name='getData'),
]