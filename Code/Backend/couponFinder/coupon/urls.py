from django.urls import path
from coupon import views

urlpatterns = [
    path('', views.coupon, name="coupon"),
]