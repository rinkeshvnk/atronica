from django.db import models
from City.models import CityModel

# Create your models here.
class ElectricianModel(models.Model):
    elec_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50,default=None)
    mobilenumber = models.CharField(max_length=50,default=None)
    img = models.CharField(max_length=100)
    city_id = models.ForeignKey(CityModel,db_column='city_id',on_delete=models.CASCADE,default=None)
    experience = models.CharField(max_length=100)
    aboutelectrician = models.CharField(max_length=400)
    isactive =  models.CharField(max_length=50)
    elec_price = models.FloatField(max_length=50,default=None)

    class Meta:
        db_table = "tbl_electrician"
