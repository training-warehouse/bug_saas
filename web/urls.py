# -*- coding: utf-8 -*-
# Time    : 2020/11/16 20:10
# Author  : LiaoKong
from django.urls import path

from web.views.account import register

app_name = 'web'

urlpatterns = [
    path('register/', register)
]
