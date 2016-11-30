# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.http import HttpResponse 
from .models import MyPortfolio

def Portfolio(request):
	mywork = MyPortfolio.objects.all().order_by("-id")
	paginator = Paginator(mywork, 4) # Show 25 contacts per page
	page = request.GET.get('page')
	try:
		work = paginator.page(page)
	except PageNotAnInteger:
		work = paginator.page(1) # If page is not an integer, deliver first page.
	except EmptyPage:
		work = paginator.page(paginator.num_pages)  # If page is out of range (e.g. 9999), deliver last page of results.
	return render(request,'ZiriPortfolio/index.html', {'work': work})
