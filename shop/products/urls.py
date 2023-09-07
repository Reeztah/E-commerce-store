from django.urls import path
from products.views import index, product_detail, category_view, faq, contact

app_name = 'products'

urlpatterns = [
    path('', index, name='index'),  # по корневому адресу .../ выводит index.html
    path('products/id/<int:pk>/', product_detail, name='product_detail'),
    # при переходе по ссылке на товар, формирует url адрес вида .../products/id/id
    path('products/categories/<int:pk>/', category_view, name='category_view'),
    path('about/', faq, name='faq'),
    path('about/contact', contact, name='contact'),
]
