from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from django.conf import settings
# Create your models here.
class certification(models.Model):
    name = models.CharField(max_length = 255,blank=True,null=True)
    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.name

class captcha(models.Model):
    id=models.ForeignKey(User, db_column="email",on_delete=models.CASCADE,primary_key=True)
    captcha=models.CharField(max_length=50,blank=True,null=True)
    def __str__(self):
        return self.captcha

class message(models.Model):
    message=models.CharField(max_length=255,blank=True,null=True)
    user=models.ForeignKey(User, db_column="username",on_delete=models.CASCADE)
    time=models.TimeField(default=now() )
    def __str__(self):
        return self.message