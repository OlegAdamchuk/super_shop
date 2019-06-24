from django.contrib import admin
from .models import Order, OrderItem
from django.shortcuts import reverse
from django.utils.html import format_html


def order_detail(obj):
    return format_html('<a href="{}">Посмотреть</a>'.format(
        reverse('order:admin_order_detail', args=[obj.id])
    ))


order_detail.short_description = 'Инфо'


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_field = ['product']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'address', 'paid', 'created',
                    order_detail]
    list_filter = ['paid', 'created', 'updated']
    inlines = [OrderItemInline]


admin.site.register(Order, OrderAdmin)
