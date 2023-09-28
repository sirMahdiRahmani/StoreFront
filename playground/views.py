from django.shortcuts import render
from django.http import HttpResponse


def say_hello(request):
    return HttpResponse("hello")


def summary(request):
    return HttpResponse(10 + 12)
