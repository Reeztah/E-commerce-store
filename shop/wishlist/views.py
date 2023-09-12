from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from wishlist.models import Wishlist, WishlistItem
from products.models import Product


@login_required
def add_to_wishlist(request, product_id):
    user = request.user
    product = Product.objects.get(id=product_id)
    wishlist, created = Wishlist.objects.get_or_create(user=user)

    # Проверка наличия товара в корзине
    wishlist_item, item_created = WishlistItem.objects.get_or_create(wishlist=wishlist, product=product)
    if not item_created:
        wishlist_item.quantity += 1
        wishlist_item.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def del_from_wishlist(request, product_id):
    user = request.user
    product = Product.objects.get(id=product_id)
    wishlist = Wishlist.objects.get(user=user)
    wishlist_item = WishlistItem.objects.get(wishlist=wishlist, product=product)
    wishlist_item.delete()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def wishlist_view(request):
    wishlist, created = Wishlist.objects.get_or_create(user=request.user)

    wishlist_items = wishlist.wishlistitem_set.all()

    context = {
        'wishlist_items': wishlist_items,
    }
    return render(request, 'wishlist/wishlist.html', context)
