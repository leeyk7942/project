# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
class BoardData(models.Model):
	boardnum = models.IntegerField(default=0)
	writer = models.CharField(max_length=30)
	title = models.CharField(max_length=300)
	contents = models.TextField()
	link = models.CharField(max_length=300, blank=True)
	files = models.FileField(blank=True)
	regdate = models.DateTimeField(auto_now_add=True)
	modifydate = models.DateTimeField(auto_now=True)

'''
class UploadFile(models.Model):
	boardidx = models.foringkey
	boardnum = models.IntegerField(default=0)
    alt = forms.CharField(max_length=50)
    file = forms.FileField()
 '''
