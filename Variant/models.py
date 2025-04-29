from django.db import models
from Products.models import ProductsModel

# Create your models here.
class VariantModel(models.Model):
    variant_id = models.AutoField(primary_key=True)
    product_id = models.ForeignKey(ProductsModel,db_column='product_id',on_delete=models.CASCADE,default=None)
    img1 = models.CharField(max_length=100)
    img2 = models.CharField(max_length=100)
    img3 = models.CharField(max_length=100)
    video_url = models.CharField(max_length=100)
    retail_price = models.FloatField(max_length=50)
    sell_price = models.FloatField(max_length=50)
    packaging = models.CharField(max_length=50)
    variant_description = models.CharField(max_length=400)

    class Meta:
        db_table = "tbl_variant"