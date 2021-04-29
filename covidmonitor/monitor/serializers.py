from rest_framework import serializers
from .models import *

class Usuario(serializers.ModelSerializer):
    class Meta:
        model = Positivo
        fields = ['email', 'temp', 'oxi', 'vali']