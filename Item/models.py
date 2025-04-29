from django.db import models
from Order.models import OrderModel
from Products.models import ProductsModel
from Variant.models import VariantModel

# Create your models here.
class ItemModel(models.Model):
    item_id = models.AutoField(primary_key=True)
    order_id = models.ForeignKey(OrderModel,db_column='order_id',on_delete=models.CASCADE,default=None)
    product_id = models.ForeignKey(ProductsModel,db_column='product_id',on_delete=models.CASCADE,default=None,null=True)
    variant_id = models.ForeignKey(VariantModel,db_column='variant_id',on_delete=models.CASCADE,default=None,null=True)
    qty = models.FloatField(max_length=100,default=None)
    price = models.FloatField(max_length=100,default=None)

    class Meta:
        db_table = "tbl_item"
