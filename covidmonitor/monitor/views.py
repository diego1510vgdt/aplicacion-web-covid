from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from .forms import *
from .models import *
import datetime
from django.contrib import messages
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
                reg.vali=True
            reg.save()
            messages.success(request, 'Registro guardado')
            return redirect('registro')
        else:
            context = {'form': form}
            return render(request, 'registro.html', context)


class Lista(View):
    def get(self, request):
        registro = Positivo.objects.all()
        busqueda = request.GET.get("buscar")
        if busqueda:
            registro = Positivo.objects.filter(
            Q(email = busqueda)
        ).distinct()
        context = {'registro' : registro}
        return render(request, 'listado.html', context)
