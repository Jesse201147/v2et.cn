# -*- coding: utf-8 -*-
# @Author : Jesse.T
# @Time   : 2019/10/12 14:15
from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']


