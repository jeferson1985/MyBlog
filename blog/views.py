from django.shortcuts import render, redirect
from .models import Materia



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