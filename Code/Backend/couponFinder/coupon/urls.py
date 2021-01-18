from django.urls import path
from . import views

urlpatterns = [
    path('', views.coupon, name="coupon"),
    path('shop_details/', views.company, name="shop_details"),
]