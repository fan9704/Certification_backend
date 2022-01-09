from django.contrib import admin
from .models import certification,message,captcha
# Register your models here.

admin.site.register(certification)
admin.site.register(message)
admin.site.register(captcha)