from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from .forms import *
from .models import *
# Create your views here.

class Home(View):
    def get(self, request):
        return render(request, 'index.html', {})

class Registro(View):
    def get(self, request):
        form = PositivoForm()
        context = {'form': form}
        return render(request, 'registro.html', context)
    
    def post(self, request):
        form = PositivoForm(request.POST)
        if form.is_valid():
            reg = form.save(commit=False)
            if (reg.temp > 37.5) or (reg.oxi < 90):
                reg.save()
            else:
                print("Todo Ok")
            return redirect('index')
        else:
            context = {'form': form}
            return render(request, 'registro.html', context)
        
