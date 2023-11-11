from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def fun1(request):
    return render(request,'third.html')
def fun2(request):
    return HttpResponse('APP3 HTTPRESPONSE')
