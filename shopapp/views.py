from django.shortcuts import render, get_object_or_404
from shopapp.models import Category, Product
from cart.forms import CartAddProductForm


def main_view(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    return render(request, 'shopapp/base.html', {
        'categories': categories,
        'products': products
    })


def product_view(request, product_slug):
    product = get_object_or_404(Product, slug=product_slug)
    cart_product_form = CartAddProductForm()
    categories = Category.objects.all()
    return render(request, 'shopapp/product.html', {
        'product': product,
        'categories': categories,
        'cart_product_form': cart_product_form
    })


def category_view(request, category_slug):
    categories = Category.objects.all()
    category = Category.objects.get(slug=category_slug)
    products_category = Product.objects.filter(category=category)
    return render(request, 'shopapp/category.html', {
        'category': category,
        'products_category': products_category,
        'categories': categories
    })
