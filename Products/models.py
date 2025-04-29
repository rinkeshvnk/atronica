from django.db import models
from Company.models import CompanyModel
from Subcategory.models import SubcategoryModel

# Create your models here.
class ProductsModel(models.Model):
    product_id = models.AutoField(primary_key=True)
    subcategory_id = models.ForeignKey(SubcategoryModel,db_column='subcategory_id',on_delete=models.CASCADE)
    company_id = models.ForeignKey(CompanyModel,db_column='company_id',on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    specification = models.CharField(max_length=400)
    description = models.CharField(max_length=400)
    retail_price = models.FloatField(max_length=50)
    sell_price = models.FloatField(max_length=50)
    img1 = models.CharField(max_length=100)
    img2 = models.CharField(max_length=100)
    img3 = models.CharField(max_length=100)
    video_url = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    packaging = models.CharField(max_length=50)
    isactive = models.CharField(max_length=50)


    class Meta:
        db_table = "tbl_products"

