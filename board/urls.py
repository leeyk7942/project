# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from board import views

app_name="board"

urlpatterns = [
    url(r'^list/(?P<num>\d+)/$', views.list, name="list"),
    url(r'^write/', views.write, name="write"),
    url(r'^read/(?P<pk>\d+)/$', views.read, name="read"),
    url(r'^update/(?P<pk>\d+)/$', views.update, name="update"),
    url(r'^delete/', views.delete, name="delete"),
]
