from django.db import models

class Order(models.Model):
    user          = models.ForeignKey('users.User', on_delete=models.SET_NULL,null=True) 
    delivery_date = models.DateField()
    recipient     = models.CharField(max_length=30)
    phone_number  = models.CharField(max_length=30)
    address       = models.CharField(max_length=300)
    point         = models.IntegerField()
    delivery_fee  = models.DecimalField(max_digits=10, decimal_places=2)
    coupon        = models.ForeignKey('users.Coupon', on_delete=models.SET_NULL, null=True)
    status        = models.ForeignKey('OrderStatus', on_delete=models.SET_NULL, null=True)
    created_at    = models.DateField(auto_now_add=True)
    total_price   = models.IntegerField()

    class Meta:
        db_table = 'orders'

class OrderItem(models.Model):
    order          = models.ForeignKey(Order, on_delete=models.CASCADE) 
    product_option = models.ForeignKey('products.ProductOption', on_delete=models.SET_NULL, null=True) 
    quantity       = models.IntegerField()
    status         = models.ForeignKey('OrderItemStatus', on_delete=models.SET_NULL, null=True) 

    class Meta:
        db_table = 'order_items' 

class OrderStatus(models.Model):
    PENDING   = 3
    COMPLETED = 6

    status =  models.CharField(max_length=20)

    class Meta:
        db_table = 'order_statuses'

class OrderItemStatus(models.Model):
    COMPLETED = 1
    SOLDOUT   = 2

    status =  models.CharField(max_length=20)

    class Meta:
        db_table = 'order_item_statuses'

class CartItem(models.Model):
    user            = models.ForeignKey('users.User', on_delete=models.CASCADE) 
    quantity        = models.IntegerField()
    product_options = models.ForeignKey('products.ProductOption', on_delete=models.CASCADE) 
    
    class Meta:
        db_table = 'cart_items'