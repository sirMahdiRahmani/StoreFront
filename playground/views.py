from django.shortcuts import render
from django.http import HttpResponse

from store.models import Product, Customer, Collection, Order, OrderItem


def say_hello(request):
    queryset = Order.objects.select_related('customer').prefetch_related('orderitem_set').order_by('-placed_at')[:5]

    return render(request, 'hello.html', {'name': "Mahdi", "orders": list(queryset)})
