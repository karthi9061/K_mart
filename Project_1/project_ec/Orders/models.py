from django.db import models
from Customers.models import Customer
from Products.models import Product
# Order

class Order(models.Model):
    LIVE=1
    DELETE=0
    DELETE_CHOICES=((LIVE,'Live'),(DELETE,'Delete'))
    CART_STAGE=0
    ORDER_CONFIRMED=1
    ORDER_PROCESSED=2
    ORDER_DELIVERED=3
    ORDER_REJECTED=4
    STATUS_CHOICES=((ORDER_CONFIRMED,'Confirmed'),
                    (ORDER_PROCESSED,'Processed'),
                    (ORDER_DELIVERED,'Delivered'),
                    (ORDER_REJECTED,'Rejected'))
    order_status=models.IntegerField(choices=STATUS_CHOICES,default=CART_STAGE)
    owner=models.ForeignKey(Customer,on_delete=models.SET_NULL,related_name='orders',null=True)
    delete_status=models.IntegerField(choices=DELETE_CHOICES, default=LIVE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
class OrderedItem(models.Model):
    product=models.ForeignKey(Product,related_name='added_carts',on_delete=models.SET_NULL,null=True)
    quantity=models.IntegerField(default=1)
    owner=models.ForeignKey(Order,related_name='added_items',on_delete=models.CASCADE)    

