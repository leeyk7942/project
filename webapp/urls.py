# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from django.contrib import admin
from webapp import settings
from main import views

app_name="webapp"
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', include('main.urls'), name="main"),
    url(r'^board/', include('board.urls'), name="board"),
] #+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
