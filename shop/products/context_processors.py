from products.models import ProductCategory, Product


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
