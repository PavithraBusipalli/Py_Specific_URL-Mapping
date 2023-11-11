from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def fun1ofapp3(request):
    return render(request,'third.html')
def fun2ofapp3(request):
    return HttpResponse('APP3 HTTPRESPONSE')
