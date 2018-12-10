from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_POST
from flora.models import Goods
from .cart import Cart
from .forms import CartAddProduct


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Goods, id=product_id)
    form = CartAddProduct(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product, quantity=1, update_quantity=cd['update'])
    return 'cart:cart_detail'


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Goods, id=product_id)
    cart.remove(product)
    return 'cart:cart_detail'

