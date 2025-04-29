from django.db import models
from django.contrib.auth.models import User
from City.models import CityModel
from datetime import datetime
# Create your models here.
class OrderModel(models.Model):
    order_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User,db_column='id',on_delete=models.CASCADE,default=None)
    total_payment = models.FloatField(max_length=50)
    address1 = models.CharField(max_length=400)
    address2 = models.CharField(max_length=400,default=None)
    pincode = models.FloatField(max_length=6)
    paytype = models.CharField(max_length=50)
    transaction_number = models.CharField(max_length=100)
    deliverycharge = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    city_id = models.ForeignKey(CityModel,db_column='city_id',on_delete=models.CASCADE,default=None)
    orderdatetime =  models.DateTimeField(default=datetime.now)

    class Meta:
        db_table = "tbl_order"