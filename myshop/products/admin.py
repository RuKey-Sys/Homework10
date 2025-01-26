from django.contrib import admin
from .models import Product

@admin.action(description="Уменьшить цену на 10%")
def reduce_price(modeladmin, request, queryset):
    for product in queryset:
        product.price *= 0.9
        product.save()

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']
    list_filter = ['price']
    search_fields = ['name']
    actions = [reduce_price]

