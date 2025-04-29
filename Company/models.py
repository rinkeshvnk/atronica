from django.db import models

# Create your models here.
class CompanyModel(models.Model):
    company_id = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=50)
    company_logo = models.CharField(max_length=100)

    class Meta:
        db_table = "tbl_company"