from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class certification(models.Model):
    name = models.CharField(max_length = 255,blank=True,null=True)
    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.field_name

class captcha(models.Model):
    id=models.ForeignKey(User,on_delete=models.CASCADE,primary_key=True)
    captcha=models.CharField(max_length=50,blank=True,null=True)
    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.field_name