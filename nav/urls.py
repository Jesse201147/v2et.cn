# -*- coding: utf-8 -*-
# @Author : Jesse.T
# @Time   : 2019/10/15 17:59
from django.urls import path

from . import views

app_name = 'nav'

urlpatterns = [
    path('',views.nav_home,name='nav_home'),
    path('search/', views.search, name='search')
]