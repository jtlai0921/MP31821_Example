# Create your views here.
# -*- coding:utf-8 -*-    
from django.http import HttpResponse
from django import template
from django.shortcuts import render

def index(request):
    return HttpResponse('歡迎來到榮欽學堂!')

#在網頁上進行計算
def calcValue(request, a, b):    
    result = int(a) + int(b)    
    return HttpResponse(str(result))

#加減乘除
def reck(request, a, b):
    num1, num2 = int(a), int(b)
    total = num1 + num2
    diff = num1 - num2
    prod = num1 * num2
    quot = num1 / num2    
    return render(request, 'reckon.html',
        {'total':total, 'diff':diff,
         'prod':prod, 'quot':quot})
    

    
    
