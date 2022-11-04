from django.shortcuts import render
from .models import Materia



def index(request):
    if request.user.is_superuser:
        Materia.objects.all()
        return render(request, 'index.html')
    else:
        Materia.objects.all()
        return render(request, 'index.html')