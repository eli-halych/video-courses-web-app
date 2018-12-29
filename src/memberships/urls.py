from django.contrib import admin
from django.urls import path

from .views import MembershipSelectView, PaymentView, UpdateTransactions, ProfileView, CancelSubscription

app_name = 'courses'

urlpatterns = [
    path('', MembershipSelectView.as_view(), name='select'),
    path('payment/', PaymentView, name='payment'),
    path('update-transactions/<subscription_id>/', UpdateTransactions, name='update-transactions'),
    path('profile/', ProfileView, name='profile'),
    path('cancel/', CancelSubscription, name='cancel'),
]
