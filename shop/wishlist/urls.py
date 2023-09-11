from django.urls import path
from wishlist.views import wishlist_view, add_to_wishlist, del_from_wishlist

app_name = 'wishlist'

urlpatterns = [
    path('', wishlist_view, name='wishlist'),
    path('add_item/<int:product_id>/', add_to_wishlist, name='add_item'),
    path('remove/<int:product_id>/', del_from_wishlist, name='remove_item'),

]
