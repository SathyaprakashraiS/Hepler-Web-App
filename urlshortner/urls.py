from django.urls import path,include
from . import views

urlpatterns=[
path("",views.home,name="home"),
path("shortnerr/",views.shortnerr,name="urlshortner"),
path("shortner/<str:url>/",views.shortner,name="urlshortner")
]