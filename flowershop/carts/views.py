from django.shortcuts import render, get_object_or_404
from products.models import Product

def cart_detail(request):
    cart = request.session.get('cart', {})
    products = []
    total = 0
    for product_id, quantity in cart.items():
        product = get_object_or_404(Product, id=product_id)
        product.quantity = quantity
        product.total_price = product.price * quantity
        total += product.total_price
        products.append(product)
    return render(request, 'carts/cart_detail.html', {'products': products, 'total': total})

