from django.shortcuts import render
from .models import *

# Create your views here.

def coupon(request):
    coupon = Coupon.objects.all()
    context = {'coupon' : coupon}
    return render(request, 'coupon/homepage.html', context)

def company(request):
    coupon = Coupon.objects.all()
    context = {'coupon' : coupon}
    return render(request, 'coupon/food.html', context)

def gadget_coupon(request):
    gadget_coupon = Gadget_coupon.objects.all()
    context = {'gadget_coupon' : gadget_coupon}
    return render(request, 'coupon/gadget.html', context)


