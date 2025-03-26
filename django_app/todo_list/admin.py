from django.contrib import admin

from .models import Products, Customer, Order, OrderItems, ShippingAddress, Category
import datetime
from django.utils import timezone

admin.site.register(Customer)
admin.site.register(Products)
admin.site.register(Order)
admin.site.register(OrderItems)
admin.site.register(ShippingAddress)
admin.site.register(Category)

class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'item', 'status', 'price', 'created_at')

class OrderItemsAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'price')