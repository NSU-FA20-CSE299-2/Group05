from django.shortcuts import render
from .models import *

# Create your views here.

def coupon(request):
   # coupon = Coupon.objects.all()
    context = {}
    return render(request, 'coupon/homepage.html', context)
