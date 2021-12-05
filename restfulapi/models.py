from django.db import models

# Create your models here.
class Product(models.Model):
    uploader = models.CharField(max_length = 30,blank=True,null=True )
    name = models.CharField(max_length = 30,blank=True,null=True )
    status = models.CharField(max_length = 15, blank=True,null=True,default='NEW')
    description = models.TextField(blank=True,null=True)
    view = models.IntegerField(blank=True,null=True)
    price = models.IntegerField(blank=True,null=True)