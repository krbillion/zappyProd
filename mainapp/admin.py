from django.contrib import admin

from .models import Product

class ProductAdmin(admin.ModelAdmin):
    date_hierarchy = 'timestamp'
    search_fields = ['title', 'price', 'description']
    list_display = ['title' ,'product_image', 'price', 'updated']
    list_editable = ['price']
    list_filter = ['price', 'timestamp']
    readonly_fields = ['updated', 'timestamp']
    prepopulated_fields = {"slug":('title',)}

    class Meta:
        model = Product

admin.site.register(Product, ProductAdmin)
