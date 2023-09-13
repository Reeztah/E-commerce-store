from django.contrib import admin
from django.urls import path
from django.urls import include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('products.urls', namespace='products')),
    path('users/', include('profiles.urls', namespace='profiles')),
    path('wishlist/', include('wishlist.urls', namespace='wishlist')),
    path('shopcart/', include('shopcart.urls', namespace='shopcart')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
