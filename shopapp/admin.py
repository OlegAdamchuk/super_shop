from django.contrib import admin

from .models import Category, Brand, Product


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']


class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'price', 'availability']
    list_filter = ['availability']
    list_editable = ['price', 'availability']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Brand)
admin.site.register(Product, ProductAdmin)
