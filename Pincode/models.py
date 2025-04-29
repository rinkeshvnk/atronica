from django.db import models

# Create your models here.
class PincodeModel(models.Model):
    pincode_id = models.AutoField(primary_key=True)
    pincode = models.FloatField(max_length=6)

    class Meta:
        db_table = "tbl_pincode"