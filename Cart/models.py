from django.db import models
from Variant.models import VariantModel
from django.contrib.auth.models import User
from Products.models import ProductsModel
from django.contrib.auth.models import User
# Create your models here.
class CartModel(models.Model):
    cart_id = models.AutoField(primary_key=True)
    qty = models.FloatField(max_length=50)
    price = models.FloatField(max_length=50)
    variant_id = models.ForeignKey(VariantModel,db_column='variant_id',on_delete=models.CASCADE,default=None,null=True)
    user_id = models.ForeignKey(User,db_column='id',on_delete=models.CASCADE,default=None)
    product_id = models.ForeignKey(ProductsModel,db_column='product_id',on_delete=models.CASCADE)


    class Meta:
        db_table = "tbl_cart"