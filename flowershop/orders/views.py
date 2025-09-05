from django.shortcuts import render,redirect
from .models import Order, OrderItem
from django.contrib.auth.decorators import login_required
from products.models import Product

@login_required
def checkout(request):
   cart = request.session.get('cart', {})
   if not cart:
       return redirect('product_list')
   
   products = []
   total = 0
   for product_id, quantity in cart.items():
        product = Product.objects.get(id=product_id)
        products.append({'product': product, 'quantity': quantity, 'subtotal': product.price * quantity})
        total += product.price * quantity

   if request.method == 'POST':
        order = Order.objects.create(customer=request.user, total=total)
        for item in products:
            OrderItem.objects.create(
               order=order, 
               product=item['product'], 
               quantity=item['quantity'], 
               price=item['product'].price
            )

        request.session['cart'] = {}
        return render(request, 'orders/confirmation.html', {'order': order})
   
@login_required
def order_success(request):
    return render(request, 'orders/order_success.html')
