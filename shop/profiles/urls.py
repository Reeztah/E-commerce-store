from django.urls import path
from profiles.views import login, register, profile, logout

app_name = 'profiles'

urlpatterns = [
    path('auth/', login, name='login'),
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
    path('logout/', logout, name='logout'),
]
