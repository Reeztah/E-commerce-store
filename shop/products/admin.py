from django.contrib import admin
from products.models import ProductCategory, SubCategory, Product

admin.site.register(ProductCategory)
admin.site.register(SubCategory)
admin.site.register(Product)
