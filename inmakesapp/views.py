from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    return render(request,'home.html')
def result(request):
    x = int(request.GET['num1'])
    y= int(request.GET['num2'])
    add = x+y
    mul = x*y
    sub = x-y
    div = x/y
    return render(request,'result.html',{'add':add,'mul':mul,'sub':sub,'div':div})


