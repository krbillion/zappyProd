from django.contrib import admin

# Register your models here.
from .models import Cart, CartItem

class CartAdmin(admin.ModelAdmin):
    class Meta:
        model = Cart

class CartItemAdmin(admin.ModelAdmin):
    class Meta:
        model = CartItem

admin.site.register(Cart, CartAdmin)

admin.site.register(CartItem, CartItemAdmin)
