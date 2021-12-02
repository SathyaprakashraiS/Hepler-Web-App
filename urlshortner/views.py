from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse,HttpResponseRedirect
from .models import *
from .serializers import *
import pyshorteners

#Create your views here.
def home(request):
	return render(request,"urlshortner.html",{})

def shortnerr(request):
	q=request.POST.get("fname")
	print("jfkkuyfjkgkgjktj",q)
	return render(request,"urlshortner.html",{})

@api_view(['GET'])
def shortner(request,url):
	Url.objects.all().update(done=2)
	slash="---"
	murl = url.replace(slash, "/")
	shortner=pyshorteners.Shortener()
	murl=shortner.tinyurl.short(murl)
	Url.objects.create(theurl=url,themurl=murl)
	shorturl = Url.objects.filter(theurl=url,done=1)
	serializer = UrlSerializer(shorturl, many=True)
	return Response(serializer.data)
	# slash="---"
	# url = url.replace(slash, "/")
	# shortner=pyshorteners.Shortener()
	# serializer=shortner.tinyurl.short(url)
	# print("intha recieve panna url:",url)
	# print("returned this url: ",serializer)
	# return Response(serializer)