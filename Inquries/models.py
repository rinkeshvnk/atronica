from django.db import models
from Electrician.models import ElectricianModel
# Create your models here.

class InquriesModel(models.Model):
    inq_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    mobile_num = models.CharField(max_length=12,default=None)
    message = models.CharField(max_length=100)
    elec_id = models.ForeignKey(ElectricianModel,db_column='elec_id',on_delete=models.CASCADE)

    class Meta:
        db_table = "tbl_inquries"
