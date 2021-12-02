from rest_framework import serializers
from .models import *
#from django.contrib.main.custom import User

class UrlSerializer(serializers.ModelSerializer):
	class Meta:
		model = Url
		fields ='__all__'
