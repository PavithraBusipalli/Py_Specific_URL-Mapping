from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def fun1ofapp2(request):
    return render(request,'second.html')
def fun2ofapp2(request):
    return HttpResponse('APP2 HTTPRESPONSE')
