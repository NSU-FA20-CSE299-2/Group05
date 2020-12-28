from django.shortcuts import render
from .models import *

# Create your views here.

def coupon(request):
    coupon = Coupon.objects.all()
    context = {'coupon':coupon}
    return render(request, 'Frontend/Backend/homepage.html')
