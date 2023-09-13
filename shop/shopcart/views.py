from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from shopcart.models import ShopCart, ShopCartItem
from products.models import Product


@login_required
def shop_cart(request):
    shopcart, created = ShopCart.objects.get_or_create(user=request.user)
    shopcart_items = shopcart.shopcartitem_set.all()
    context = {
        'shopcart_items': shopcart_items
    }
    return render(request, 'shopcart/shopcart.html', context)


@login_required
def add_to_cart(request, product_id):
    user = request.user
    product = Product.objects.get(id=product_id)
    shopcart, created = ShopCart.objects.get_or_create(user=user)
    shopcart_item, item_created = ShopCartItem.objects.get_or_create(shopcart=shopcart, product=product)

    if not item_created:
        shopcart_item.quantity += 1
        shopcart_item.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def del_from_cart(request, product_id):
    user = request.user
    product = Product.objects.get(id=product_id)
    shopcart = ShopCart.objects.get(user=user)
    shopcart_item = ShopCartItem.objects.get(shopcart=shopcart, product=product)

    try:
        shopcart_item.delete()
    except ShopCartItem.DoesNotExist:
        return []

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
