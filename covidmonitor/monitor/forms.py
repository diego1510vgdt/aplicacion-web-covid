from django import forms
from .models import *

class PositivoForm(forms.ModelForm):
    class Meta:
        model = Positivo
        fields = '__all__'
