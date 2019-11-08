# -*- coding: utf-8 -*-
# @Author : Jesse.T
# @Time   : 2019/10/11 17:30
from django.urls import path
from . import views

app_name = 'userprofile'
urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('register/', views.user_register, name='register'),
    path('delete/<int:id>/', views.user_delete, name='delete'),
    path('edit/<int:id>/', views.profile_edit, name='edit'),
    path('activate/<str:activate_str>/', views.user_activate, name='activate')
    # path('register_check',views.register_check,name='register_check'),
]
