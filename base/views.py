from django.shortcuts import render
from django.http import HttpResponse

def taskList(request):
    return HttpResponse('Just trying with some function based view.')

