from django.urls import path
from . import views


urlpatterns = [
    path('create/', views.order_create, name='order_create'),
    path('admin/order/<int:order_id>/', views.admin_order_detail, name='admin_order_detail'),
    # path(r'^admin/order/(?P<order_id>\d+)/pdf/$', views.AdminOrderPDF, name='AdminOrderPDF')
]