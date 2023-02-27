from django.contrib import admin

from ecom_app.models import Product


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'quantity', 'price')
    list_filter = ('id', 'name', 'category', 'quantity', 'price')
    search_fields = ('category', 'name', 'price')
    list_editable = ('name', 'price', 'quantity')


admin.site.register(Product, ProductAdmin)
