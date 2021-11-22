from django.contrib import admin

from .models import Category, Product

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "price",
        "category",
        "sold_out",
        "quantity_available",
        "unique",
        "sku",
        "dimensions",
    )
    list_editable = ["price", "quantity_available", "sold_out"]


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "friendly_name",
        "name",
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
