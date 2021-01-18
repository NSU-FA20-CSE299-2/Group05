from django.urls import path
from . import views

urlpatterns = [
    path('', views.coupon, name="coupon"),
    path('food/', views.company, name="food"),
]