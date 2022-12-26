from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def ram(request):
    return HttpResponse('second in first')
def man(request):
    return HttpResponse('second in second')