# -*- coding: utf-8 -*-
# @Author : Jesse.T
# @Time   : 2019/10/15 13:36

from django.shortcuts import redirect

def home_page(request):
    return redirect('nav:nav_home')
