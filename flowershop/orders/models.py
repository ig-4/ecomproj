from django.db import models
from django.contrib.auth.models import User
from products.models import Product

class Order(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('SHIPPED', 'Shipped'),
        ('DELIVERED', 'Delivered'),
    ]
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)    
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='PENDING')
    total = models.DecimalField(max_digits=10, decimal_places=2)    

    def __str__(self):
        return f"Order {self.id} by {self.customer.username}"   
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)    

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"
