from django.db import models

# Create your models here.
class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=30)
    product_des = models.CharField(max_length=200)
    product_date = models.DateField()
    price = models.IntegerField(default=0)
    image= models.ImageField(upload_to='mall/images',default='')

    def __str__(self):
        return self.product_name