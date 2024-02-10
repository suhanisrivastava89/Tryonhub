from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('signup',views.signup, name='signup'),
    path('login2', views.login, name='login2'),
    path('logout', views.logout,name='logout'),
    path('products', views.products,name='products'),
    path('cart', views.cart,name='cart'),
    path('mainproducts',views.mainproducts,name='mainproducts')
]