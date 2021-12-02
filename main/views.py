from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse,HttpResponseRedirect
from .models import *

#Create your views here.
def home(request):
	return render(request,"home.html",{})