from django.shortcuts import render
from django.db.models import Value, F, Func, Count, Max, Min, Sum, ExpressionWrapper, DecimalField
from django.db.models.functions import Concat
from store.models import Product, Customer, Collection, Order, OrderItem


def say_hello(request):
    result = Product.objects.annotate(
        total_sell=Sum(
            F('orderitem__unit_price') *
            F('orderitem__quantity')
        )
    ).filter(total_sell__isnull=False).order_by('-total_sell')[0:5]
    return render(request, 'hello.html', {'name': "Mahdi", "result": result})
