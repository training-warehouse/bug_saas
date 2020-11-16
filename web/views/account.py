# -*- coding: utf-8 -*-
# Time    : 2020/11/15 17:11
# Author  : LiaoKong

from django.shortcuts import render

from web.forms.account import RegisterModelForm


def register(request):
    form = RegisterModelForm()
    return render(request, 'register.html', {'form': form})
