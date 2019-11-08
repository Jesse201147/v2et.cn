# -*- coding: utf-8 -*-
# @Author : Jesse.T
# @Time   : 2019/10/11 16:39
from django import forms
from .models import ArticlePost


class ArticlePostForm(forms.ModelForm):
    class Meta:
        model = ArticlePost
        fields = ('title', 'body','tags','avatar')
