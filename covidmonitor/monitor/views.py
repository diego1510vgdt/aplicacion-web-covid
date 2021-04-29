from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views import View
from .forms import *
from .models import *
import datetime, requests
from django.contrib import messages
from rest_framework import viewsets
from .serializers import Usuario

class Home(View):
    def get(self, request):
        response = requests.get('https://covidtracking.com/api/states')
        response1 = requests.get('https://api.covidtracking.com/v1/us/current.json')
        response2 = requests.get('https://api.apify.com/v2/key-value-stores/moxA3Q0aZh5LosewB/records/LATEST?disableRedirect=true')
        grafica = ['NY', 'CA', 'IL', 'TX', 'AZ', 'PA', 'NC', 'OH', 'FL', 'IN']
        data = []
        for state in response.json():
            for st in grafica:
                if state['state'] == st:
                    data.append(state['positive'])
        print(data)
        context = {
            'lista_estados' : response.json(),
            'datosEUpn' : response1.json(),
            'datosEUtm' : response2.json(),
            'data' : data
        }
        return render(request, 'index.html', context)

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
                messages.success(request, 'Positivo para SARS-CoV2')
            reg.save()
            return redirect('registro')
        else:
            context = {'form': form}
            return render(request, 'registro.html', context)

class Lista(View):
    def get(self, request):
        registro = Positivo.objects.all()
        context = {'registro' : registro}
        return render(request, 'listado.html', context)

class RegistroViewSet(viewsets.ModelViewSet):
    queryset = Positivo.objects.all().order_by('timestamp')
    serializer_class = Usuario

