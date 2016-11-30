# -*- coding: utf-8 -*-
from django.forms import ModelForm
from .models import BoardData

class boardForm(ModelForm):
	class Meta:
		model = BoardData
		fields = ('boardnum', 'writer', 'title', 'contents', 'link', 'files')
