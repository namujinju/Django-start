from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    return HttpResponse("Hello World!")


def select(request):
    message = "수 하나 입력"
    return HttpResponse(message)


def result(request):
    message = "추첨 결과입니다."
    return HttpResponse(message)