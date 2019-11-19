#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# author : frontier8186 time: 2019/11/12
from django.conf.urls import url
from . import views


urlpatterns ={
    url(r'moments_input', views.moments_input),
    url(r'', views.welcome),
}