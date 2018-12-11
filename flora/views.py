from django.shortcuts import render
from django.http import HttpResponse
from flora.models import Goods, Order, OrderGoods
from flora.image_resize import resizing
from floraperm.settings import BASE_DIR
import os
from cart.cart import Cart
import json
from .forms import DeliveryForm


def index(request):

    photo_checker()
    last_goods = Goods.objects.order_by('pub_date').reverse()[0:4]

    context = {
        'title': 'flora!',
        'goods_counter': 0,
        'total_price': 0,
        'categories': Goods.GOODS_TYPES,
        'last_goods': last_goods
    }

    return render(request,'index.html', context)


def catalog(request):
    photo_checker()
    all_goods = Goods.objects.all()
    context = {
        'title': 'Каталог',
        'categories': Goods.GOODS_TYPES,
        'Goods': all_goods,
    }

    cart = Cart(request)
    cart_list = [item for item in cart]


    return render(request, 'catalog.html', context)


def catalog_categories(request, category):
    photo_checker()
    main_header = [i[1] for i in Goods.GOODS_TYPES if i[0] == category][0]
    goods_category = Goods.objects.filter(goods_type=category)
    context = {
        'title': category,
        'categories': Goods.GOODS_TYPES,
        'Goods': goods_category,
        'header': main_header,
    }
    return render(request, 'catalog-categories.html', context)


def checkout(request):

    if request.method == 'POST':
        form = DeliveryForm(request.POST)
        if form.is_valid():
            cart = Cart(request)
            add_order(form, cart)
            return index(request)

    else:
        form = DeliveryForm()
        context = {
            'form': form,
            'title': 'Оформление заказа',
            'categories': Goods.GOODS_TYPES,
            'cart': Cart(request)
        }

    return render(request, 'checkout.html', context)


def photo_checker():
    unchecked = Goods.objects.filter(photo_checked=False)
    if len(unchecked) > 0:
        for un in unchecked:
            path = os.path.join(BASE_DIR,str(un.goods_photo))
            un.photo_checked = True
            resizing(path)


def add_goods(request):
    if request.method == 'POST':
        cart = Cart(request)
        g_id = int(request.POST.get('id'))
        product = Goods.objects.filter(goods_id=g_id)[0]
        cart.add(product)

        response_data = {
            'total_price': cart.get_total_price(),
            'goods_counts': len(cart),
            'product': {
                'product_name': product.goods_name,
                'total_price': product.price,
                'product_id': product.goods_id
            }
        }

        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )


def remove_goods(request):
    if request.method == 'POST':
        cart = Cart(request)
        prod_id = request.POST.get('id')

        cart.remove(prod_id=prod_id)

        response_data = {
            'total_price': cart.get_total_price(),
            'goods_counts': len(cart)
        }

        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )


def add_order(form, cart):
    name = form.cleaned_data['name']
    surname = avoid_key_error(form, 'surname')
    phone_num = form.cleaned_data['phone_num']
    address = form.cleaned_data['street'] + ' ' + \
              form.cleaned_data['street_number'] + ', ' + avoid_key_error(form, 'flat_number')
    comment = avoid_key_error(form, 'comment')

    for item in cart:
        g = Goods.objects.filter(goods_id=item['product_id'])[0]
        og = OrderGoods(product=g, quantity=item['quantity'])
        og.save()

    order = Order(customer_name=name+' '+surname, phone_num=phone_num,
                  address=address, total_sum=cart.get_total_price(), comment=comment )
    order.save()
    goods = OrderGoods.objects.order_by('id').reverse()[0:len(cart)]
    [order.goods.add(i) for i in goods]

    cart.clear()


def avoid_key_error(form, st):
    try:
        item = form.cleaned_data[st]
        return item
    except KeyError:
        return ''
