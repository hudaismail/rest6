from django.urls import path
from . import views

urlpatterns = [
    path("pay/", views.start_payment, name="start_payment"),
    path("callback/", views.payment_callback, name="payment_callback"),
]

"""   
   path('payment_success', views.payment_success, name='payment_success'),
   path('payment_failed', views.payment_failed, name='payment_failed'),
"""

