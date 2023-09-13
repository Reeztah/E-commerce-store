from products.models import ProductCategory, Product
from wishlist.models import Wishlist, WishlistItem
from shopcart.models import ShopCart, ShopCartItem


def categories(request):
    categories = ProductCategory.objects.all()
    return {'categories': categories}


def footer_filter(request):
    iphones = Product.objects.filter(new_product=True, category_id=1)
    macs = Product.objects.filter(new_product=True, category_id=2)
    ipads = Product.objects.filter(new_product=True, category_id=3)
    watches = Product.objects.filter(new_product=True, category_id=4)
    airpods = Product.objects.filter(new_product=True, category_id=5)
    return {
        'iphones': iphones,
        'macs': macs,
        'ipads': ipads,
        'watches': watches,
        'airpods': airpods,
    }


def wishlist_count(request):
    if request.user.is_authenticated:
        wishlist = Wishlist.objects.get(user=request.user)
        wishlist_item_count = WishlistItem.objects.filter(wishlist=wishlist).count()
    else:
        return {}

    return {'wishlist_count': wishlist_item_count}


def shopcart_count(request):
    if request.user.is_authenticated:
        shopcart = ShopCart.objects.get(user=request.user)
        shopcart_item_count = ShopCartItem.objects.filter(shopcart=shopcart).count()
    else:
        return {}

    return {'shopcart_count': shopcart_item_count}
