from django.db import models
from Category.models import CategoryModel
# Create your models here.
class SubcategoryModel(models.Model):
    subcategory_id = models.AutoField(primary_key=True)
    subcategory_name = models.CharField(max_length=50)
    category_id = models.ForeignKey(CategoryModel,db_column='category_id',on_delete=models.CASCADE)


    class Meta:
        db_table = "tbl_subcategory"