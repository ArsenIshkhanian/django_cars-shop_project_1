from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('product/<int:id>/', views.product, name='product'),
    path('cart/', views.cart, name='cart'),
    path('add_cart/<str:cat_name>/', views.add_cart, name='add_cart'),
    path('del_item/', views.del_item, name='del_item')
]