# -*- coding: utf-8 -*-
# @Author : Jesse.T
# @Time   : 2019/10/12 14:10
from django.urls import path
from . import views

app_name = 'comment'

urlpatterns = [
    path('post-comment/<int:article_id>/',views.post_comment,name='post_comment'),
    path('post-comment/<int:article_id>/<int:parent_comment_id>',views.post_comment,name='comment_reply'),
]

