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


