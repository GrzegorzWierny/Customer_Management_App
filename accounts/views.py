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


def costumer(requeste):
    return render(requeste, 'accounts/costumer.html')

