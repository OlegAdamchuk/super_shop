from django.urls import path

from . import views

urlpatterns = [
    path('category/<slug:category_slug>/', views.category_view, name='category_detail'),
    path('product/<slug:product_slug>/', views.product_view, name='product_detail'),
    path('', views.main_view, name='base'),
]
