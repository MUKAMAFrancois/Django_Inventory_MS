from django.db import models
from django.contrib.auth.models import User

# Create your models here.


category=(('laptops','Laptops'),
          ('desktops','Desktops'),
          ('phones','SmartPhones'),
          ('accessories','Accessories'))

class ProductModel(models.Model):

    product_name=models.CharField(max_length=200, help_text='Name or S/N')
    qty=models.PositiveIntegerField()
    category=models.CharField(max_length=90,choices=category, default='phones')
    time_of_purchase=models.DateTimeField(auto_created=True)


    def __str__(self) -> str:
        return self.product_name
    
class OrderModel(models.Model):
    name_product=models.ForeignKey(ProductModel,on_delete=models.CASCADE)
    client_name=models.ForeignKey(User, on_delete=models.CASCADE)
    qty_ordered=models.PositiveIntegerField()
    time_of_order=models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.client_name} => {self.name_product}'
