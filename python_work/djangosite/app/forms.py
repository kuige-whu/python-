#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# author : frontier8186 time: 2019/11/12 
from django.forms import ModelForm
from app.models import Moment


class MomentForm(ModelForm):
    class Meta:
        model = Moment
        fields = '__all__'
        # 导入所有字段
        # fields=('content', 'user_name',  'kind')
