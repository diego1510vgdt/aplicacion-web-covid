from django.urls import path
from .views import *

urlpatterns = [
    path('', Home.as_view() , name='index'),
    path('registro', Registro.as_view() , name='registro'),
]

