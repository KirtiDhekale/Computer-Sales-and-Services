from django.db import models


class Product(models.Model):
    pname = models.TextField(primary_key=True)
    pdescription = models.TextField()

    class Meta:
        db_table = 'tblProduct'

