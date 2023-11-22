from django.shortcuts import render
from django.http import HttpResponse

from store.models import Product, Customer, Collection, Order, OrderItem


def say_hello(request):
    queryset = Product.objects.filter(id__in=OrderItem.objects.values('product_id').distinct()).order_by('title')

    return render(request, 'hello.html', {'name': "Mahdi", "products": list(queryset)})
