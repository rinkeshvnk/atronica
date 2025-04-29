from django.db import models
from State.models import StateModel

# Create your models here.
class CityModel(models.Model):
    city_id = models.AutoField(primary_key=True)
    state_id = models.ForeignKey(StateModel,db_column='state_id',on_delete=models.CASCADE)
    city_name = models.CharField(max_length=50)

    class Meta:
        db_table = "tbl_city"