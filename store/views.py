from django.shortcuts import render
from django.db import transaction
from django.db.models import Value, F, Func, Count, Max, Min, Sum, ExpressionWrapper, DecimalField
from django.db.models.functions import Concat
from store.models import Product, Customer, Collection, Order, OrderItem, Cart, CartItem


def say_hello(request):
    queryset = Product.objects.annotate(
        discounted_price=ExpressionWrapper(F('unit_price') * 0.8, output_field=DecimalField()))

    return render(request, 'hello.html', {'name': "Mahdi", "data": list(queryset)})
