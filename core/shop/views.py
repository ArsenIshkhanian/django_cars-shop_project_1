from django.shortcuts import render, redirect
from .models import Category, Product, Cart

# Create your views here.

def index(request):
    category_list = Category.objects.all()
    return render(request, 'shop/index.html', context={
        'category_list': category_list
    })


def product(request, id):
    prod_list = Category.objects.get(pk=id)
    return render(request, 'shop/product.html', context={
        'prod_list':prod_list,
    })

def add_cart(request, cat_name):
    if request.method == 'POST':
        cat_id = Category.objects.get(name=cat_name).id
        product_id = request.POST.get('prod_id')
        prod = Product.objects.get(id=product_id)
        Cart.objects.create(prod_id=prod)
        return redirect('product', id=cat_id)

def cart(request):
    cart_list = Cart.objects.all()
    return render(request, 'shop/cart.html', context={
        'cart_list': cart_list
    })


def del_item(request):
    if request.method == 'POST':
        cart_id = request.POST.get('cart_del')
        Cart.objects.get(id=cart_id).delete()
        return redirect('cart')