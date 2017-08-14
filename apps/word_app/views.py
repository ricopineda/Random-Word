# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
import random
from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime
from django.contrib import messages
from django.utils.crypto import get_random_string
# the index function is called when root is visited
def index(request):
	print 'hello'
	return render(request,'word_app/index.html')

# def create(request):
# 	if request.method == "POST":
# 		print "hello"

# 		return redirect("word_app/index.html")

def create(request):
	count = 0


	if request.method == "POST":

		request.session['ran_word'] = get_random_string(length=14)
		print request.session['ran_word']
		
		request.session['counter'] += count + 1
		print request.session['counter']
		
		
		return redirect("/")
	else:
		return redirect("/")



