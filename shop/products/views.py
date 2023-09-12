from django.shortcuts import render
from wishlist.models import Wishlist
from products.models import ProductCategory, Product


def index(request):
    context = {
        'new_products': Product.objects.filter(new_product=True),
    }
    return render(request, 'products/index.html', context)


def faq(request):
    return render(request, 'products/faq.html')


def contact(request):
    return render(request, 'products/contact.html')


def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    category_name = product.category  # Получить категорию товара

    if request.user.is_authenticated:
        wishlist = Wishlist.objects.filter(user=request.user)
        product_in_wishlist = wishlist.filter(wishlistitem__product=product).exists()
        context = {
            'product_in_wishlist': product_in_wishlist,
            'category_name': category_name,
            'product': product,
        }
        return render(request, 'products/product_view.html', context)

    context = {
        'product': product,
        'category_name': category_name,

    }
    return render(request, 'products/product_view.html', context)


def category_view(request, pk):
    category = ProductCategory.objects.get(pk=pk)
    products = Product.objects.filter(category=category)
    context = {
        'category': category,
        'products': products,
    }
    return render(request, 'products/category_view.html', context)
