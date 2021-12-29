from django.db import models

# Create your models here.
class certification(models.Model):
    name = models.CharField(max_length = 255,blank=True,null=True)