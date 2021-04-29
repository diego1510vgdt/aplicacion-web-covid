from django.urls import path, include
from .views import *
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'api/v1', RegistroViewSet)

urlpatterns = [
    path('', Home.as_view() , name='index'),
    path('registro', Registro.as_view() , name='registro'),
    path('lista', Lista.as_view() , name='lista'),
    path('', include(router.urls)),
]

