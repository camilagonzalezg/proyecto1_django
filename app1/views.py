from django.shortcuts import render
from datetime import datetime

def index(request):
    return render(request, 'index.html')

def fecha_actual(request):
    now = datetime.now()
    context = {'fecha_actual': now}
    return render(request, 'fecha-actual.html', context)