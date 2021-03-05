from django.db import models
from django.conf import settings
# Create your models here.

class Shop(models.Model):
    shop_id = models.AutoField
    shop_name = models.CharField(max_length=50)
    details = models.CharField(max_length=300)
    address = models.CharField(max_length=500, default="")
    contact = models.IntegerField(default=0)
    pincode = models.IntegerField(default=700075)
    image = models.ImageField(upload_to='shop/images', default="")

    def __str__(self):
        return self.shop_name


class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default="")
    subcategory = models.CharField(max_length=50, default="")
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=300)
    pub_date = models.DateField()
    image = models.ImageField(upload_to='shop/images', default="")
    shop=models.ForeignKey(Shop,on_delete=models.CASCADE, default=0)
    review = models.IntegerField(default=4)

    def __str__(self):
        return self.product_name



class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    phone = models.CharField(max_length=70, default="")
    desc = models.CharField(max_length=500, default="")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.CASCADE)

    def __str__(self):
        return self.name

class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    items_json = models.CharField(max_length=5000)
    amount = models.IntegerField( default=0)
    name = models.CharField(max_length=90)
    email = models.CharField(max_length=111)
    address = models.CharField(max_length=111)
    city = models.CharField(max_length=111)
    state = models.CharField(max_length=111)
    zip_code = models.CharField(max_length=111)
    phone = models.CharField(max_length=111, default="")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.CASCADE)

class OrderUpdate(models.Model):
    update_id  = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default="")
    update_desc = models.CharField(max_length=5000)
    timestamp = models.DateField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.update_desc[0:7] + "..."
