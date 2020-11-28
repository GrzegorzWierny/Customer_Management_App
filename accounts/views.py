from django.shortcuts import render
from django.http import HttpResponse
from .models import *


def home(requeste):
    orders = Order.objects.all()
    costumers = Customer.objects.all()

    total_costumers = costumers.count()
    total_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()

    context = {'orders': orders,
               'costumers': costumers,
               'total_costumers': total_costumers,
               'total_orders': total_orders,
               'delivered': delivered,
               'pending': pending,
               }
    return render(requeste, 'accounts/dashboard.html', context)


def products(requeste):
    products: object = Product.objects.all()

    return render(requeste, 'accounts/products.html', {'products': products})


def customer(requeste, pk_test):
    customer = Customer.objects.get(id=pk_test)

    orders = customer.order_set.all()
    order_count = orders.count()

    context = {'customer': customer, 'orders': orders, 'order_count': order_count}
    return render(requeste, 'accounts/costumer.html', context)

