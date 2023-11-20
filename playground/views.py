from django.shortcuts import render
from django.http import HttpResponse

from store.models import Product, Customer, Collection, Order, OrderItem


def say_hello(request):
    query_set = OrderItem.objects.filter(product__collection__id=3)

    return render(request, 'hello.html', {'name': "Mahdi", "orderitems": list(query_set)})


def summary(request):
    return HttpResponse(10 + 12)
