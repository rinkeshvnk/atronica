from django.db import models

# Create your models here.
class UserModel(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=50)
    otp = models.FloatField(max_length=10)
    isactive = models.CharField(max_length=10)
    mobile = models.FloatField(max_length=12)

    class Meta:
        db_table = "tbl_user"

