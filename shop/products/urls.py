from django.urls import path
from products.views import index, product_detail, category_view, faq, contact

app_name = 'products'

urlpatterns = [
    path('', index, name='index'),
    path('products/product_detail/<int:pk>/', product_detail, name='product_detail'),
    path('products/categories/<int:pk>/', category_view, name='category_view'),
    path('about/', faq, name='faq'),
    path('about/contact', contact, name='contact'),
]
