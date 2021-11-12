from django.contrib import admin

from .models import Category, Product

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "price",
        "category",
        "quantity_available",
        "unique",
        "sku",
        "dimensions",
    )
    list_editable = ["price", "quantity_available"]


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "friendly_name",
        "name",
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
