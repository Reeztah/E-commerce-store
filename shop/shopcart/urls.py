from django.urls import path
from shopcart.views import shop_cart, add_to_cart, del_from_cart
app_name = 'shopcart'

urlpatterns = [
    path('', shop_cart, name='shopcart'),
    path('add_item/<int:product_id>/', add_to_cart, name='add_item'),
    path('remove/<int:product_id>/', del_from_cart, name='remove_item'),

]
