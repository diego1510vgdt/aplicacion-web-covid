from django import forms
from .models import *

class PositivoForm(forms.ModelForm):
    class Meta:
        model = Positivo
        fields = ['email', 'temp', 'oxi']
        #fields = ['email', 'temp', 'oxi']
