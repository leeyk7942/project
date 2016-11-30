# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.template import Context
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from .forms import *

#********************************************************************************
#최종수정일 : 2016-11-24
#********************************************************************************
def list(request, num):
	bnum = request.GET.get(num)

	return HttpResponse(bnum)
'''
# 게시물 리스트 목록
def list(request, num):
	bnum = request.GET.get(num)
	boarddata = BoardData.objects.filter(boardnum=bnum).order_by('-id')
	context = Context({'boarddata':boarddata})
	return render(request, 'board/list.html', context)
'''
#********************************************************************************

# 게시물 작성
def write(request):
	if request.method == "POST":
		form = boardForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('board:list')
	else:
		form = boardForm()
		context = Context({'form':form})
	return render(request, 'board/write.html', context)

#********************************************************************************

# 게시물 업데이트
def update(request, pk):
	boarddata = BoardData.objects.get(pk=pk)
	if request.method == "POST":
		form = boardForm(request.POST, instance=boarddata)
		if form.is_valid():
			form.save()
			return redirect('board:read', pk)
	else:
		form = boardForm(instance=boarddata)
		context = Context({'form':form}, {'boarddata':boarddata})
		return render(request, 'board/edit.html', context)

#********************************************************************************

# 게시물 상세페이지
def read(request, pk):
	boarddata = BoardData.objects.get(pk=pk)
	context = Context({'boarddata':boarddata})
	return render(request, 'board/read.html', context)

#********************************************************************************

# 게시물 삭제
def delete(request):
	return HttpResponse('delete')
