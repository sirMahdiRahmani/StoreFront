from django.shortcuts import render
from django.http import HttpResponse

from store.models import Product


def say_hello(request):
    query_set = Product.objects.all()

    print(query_set[0])

    return HttpResponse("hello")


def summary(request):
    return HttpResponse(10 + 12)
