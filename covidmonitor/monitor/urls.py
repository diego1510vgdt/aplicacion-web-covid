from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('', Home.as_view() , name='index'),
    path('registro', Registro.as_view() , name='registro'),
    path('lista', Lista.as_view() , name='lista'),
]

