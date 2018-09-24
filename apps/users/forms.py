# -*- coding: utf-8 -*-
from django import forms

__author__ = 'ysir'
__date__ = '2018/8/25 11:00'


class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=5)
