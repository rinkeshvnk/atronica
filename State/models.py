from django.db import models

# Create your models here.
class StateModel(models.Model):
    state_id = models.AutoField(primary_key=True)
    state_name = models.CharField(max_length=50)

    class Meta:
        db_table = "tbl_state"