from django.db import models

# Create your models here.
class Url(models.Model):
	theurl=models.CharField(max_length=1000,default="url")
	themurl=models.CharField(max_length=1000,default="murl")
	done=models.IntegerField(default=1)