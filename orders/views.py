from rest_framework import viewsets
from django.shortcuts import render
from .models import Customer, Order
from .serializers import CustomerSerializer, OrderSerializer

from .utils import send_sms


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


def add_order(request):
    order = Order.objects.create(customer=request.user, item='Product X', amount=50)

    # Send SMS alert to the customer
    message = f"Dear {order.customer.name}, your order ({order.item}) has been placed successfully. Thank you!"
    send_sms(order.customer.phone_number, message)

    return render(request, 'order_added.html', {'order': order})
