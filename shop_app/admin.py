from django.contrib import admin
from .models import Client, Product, Order


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'quantity']
    ordering = ['category', '-quantity']
    list_filter = ['date_added', 'price']
    search_fields = ['description']
    search_help_text = 'Поиск по полю Описание продукта (description)'


class ClientAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']
    ordering = ['date']
    list_filter = ['date']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['total_price']
    ordering = ['order_date']
    list_filter = ['order_date', 'total_price']
    search_fields = ['client']


class ProductsAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'product_price', 'product_description']
    ordering = ['product_add_date', '-product_quantity', 'product_quantity']
    list_filter = ['product_add_date', 'product_price']
    search_fields = ['product_photo']


admin.site.register(Client)
admin.site.register(Product)
admin.site.register(Order)
# Register your models here.
