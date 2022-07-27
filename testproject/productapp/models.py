from django.db import models


# Create your models here.
class Products(models.Model):
    name = models.CharField(max_length=150, null=False, blank=False)
    image = models.ImageField(upload_to="productapp/uploads", null=False, blank=True)