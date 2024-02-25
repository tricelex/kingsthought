
from django.urls import path

from lynx.views import index, dashboard, register, login, profile, logout

urlpatterns = [
    path('', index, name='index'),
    path('register', register, name='register'),
    path('login', login, name='login'),
    path('logout', logout, name='logout'),
    path('dashboard', dashboard, name='dashboard'),
    path('profile', profile, name='profile'),
]