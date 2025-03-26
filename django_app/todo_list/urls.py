from django.urls import path
from .import views

urlpatterns = [
   path('', views.index, name='index'),
   path('home', views.home, name='home'),
   path('about', views.about, name='about'),
   path('contact', views.contact, name='contact'),
   path('category/<str:foo>', views.category,name='category'),
   path('search', views.search, name='search'),
   path('cart/', views.cart, name='cart'),
   path('checkout', views.checkout, name='checkout'),
   path('update_item/', views.updateItem, name='update_item'),
   path('process_order/', views.processOrder, name='process_order'),

]

"""   
   path('payment_success', views.payment_success, name='payment_success'),
   path('payment_failed', views.payment_failed, name='payment_failed'),
"""

