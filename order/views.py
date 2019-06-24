from django.shortcuts import render, get_object_or_404
from .models import OrderItem, Order
from .forms import OrderCreateForm
from django.contrib.admin.views.decorators import staff_member_required
from cart.cart import Cart


@staff_member_required
def admin_order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'admin/order/detail.html', {'order': order})


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.save()
            for item in cart:
                OrderItem.objects.create(order=order, product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            cart.clear()

            request.session['order_id'] = order.id
            return render(request, 'order/created.html', {'order': order})

    form = OrderCreateForm()
    return render(request, 'order/create.html', {'cart': cart,
                                                 'form': form})
