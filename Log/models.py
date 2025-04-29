from django.db import models
from Order.models import OrderModel


# Create your models here.
class LogModel (models.Model):
    log_id = models.AutoField(primary_key=True)
    order_id = models.ForeignKey(OrderModel,db_column='order_id',on_delete=models.CASCADE)
    status = models.CharField(max_length=40)

    class Meta:
        db_table = "tbl_log"


