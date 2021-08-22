from django.contrib import admin
from django.urls import path
from django.urls import re_path

from django.urls import path, include
from django.contrib import admin
from .views import *
from django.urls import re_path




urlpatterns = [

    path('index/', post_index, name = 'index'),
    re_path(r'^(?P<id>\d+)/$', post_detail, name = 'detail'),
    path('create/', post_create, name = 'create'),
    re_path(r'^(?P<id>\d+)/update/$', post_update, name = 'update'),
    re_path(r'^(?P<id>\d+)/delete/$', post_delete, name = 'delete'),

 ]

