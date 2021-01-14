from django.db import models

# Create your models here.
class TabelaBin(models.Model):
    informacao_bin_primary_key = models.AutoField(primary_key=True)
    numero = models.IntegerField()
    issuer_name = models.CharField(max_length=40)
    product_name = models.CharField(max_length=40)
    brand_name = models.CharField(max_length=40)
    country = models.CharField(max_length=40)
    is_international = models.BooleanField(default=False)
    is_company = models.BooleanField(default=False)
    is_token = models.BooleanField(default=False)

