from django.shortcuts import render, redirect
from .models import Materia
from django.contrib.auth.decorators import login_required



@login_required(redirect_field_name='logar')
def index(request):
    if request.user.is_superuser:
        materias = Materia.objects.all()
        return render(request, 'index.html', {'materias':materias})
    else:
        materias = Materia.objects.all()
        return render(request, 'index.html', {'materias':materias})
    
    
def buscar(request):
    termo = request.GET.get('termo')#name="termo" no html
    materias = Materia.objects.filter(titulo__icontains=termo)#icontains usado para filtrar
    return  render(request, 'index.html', {'materias': materias})


def nova_publicacao(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        descricao = request.POST.get('descricao')
        categoria = request.POST.get('categoria')
        data_publicacao = request.POST.get('data_publicacao')
        imagem = request.FILES.get('imagem')
        
        Materia.objects.create( autor=request.user, titulo=titulo, descricao=descricao, categoria=categoria, data_publicacao=data_publicacao, imagem=imagem)
        return redirect('blog')
    else:
        return render(request, 'nova_publicacao.html')
    
    
def info_materia(request, id):
        materias = Materia.objects.get(id=id)
        titulo = request.POST.get('titulo')
        descricao = request.POST.get('descricao')
        categoria = request.POST.get('categoria')
        data_publicacao = request.POST.get('data_publicacao')
        imagem = request.POST.get('imagem')
        
        Materia.objects.get(titulo=titulo, descricao=descricao, categoria=categoria, data_publicacao=data_publicacao, imagem=imagem)
        return render(request, 'info_materia.html', {'materias:':materias})