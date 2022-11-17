from django.shortcuts import render, redirect
from .models import Materia
from django.contrib.auth.decorators import login_required
from .models import Comentario, Favoritos



@login_required(redirect_field_name='logar')
def index(request):
    if request.user.is_superuser:
        materias = Materia.objects.all().order_by('-id')
        return render(request, 'index.html', {'materias':materias})
    else:
        materias = Materia.objects.all()
        return render(request, 'index.html', {'materias':materias})
    
def home(request):
    materias = Materia.objects.all().order_by('-id')
    return render(request, 'index.html',{'materias':materias})
    
    
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
        
        Materia.objects.create(autor=request.user, titulo=titulo, descricao=descricao, categoria=categoria, data_publicacao=data_publicacao, imagem=imagem)
        return redirect('blog')
    else:
        return render(request, 'nova_publicacao.html')
    
    
def info_materia(request, id):
    materia = Materia.objects.get(id=id)
    comentarios = Comentario.objects.filter(pk_materia=id)
    return render(request, 'info_materia.html', {'materia':materia, 'comentarios':comentarios})


def get_comentario(request, id):
    materia = Materia.objects.get(id=id)
    return render(request, 'comentario.html',{'materia':materia})
    

    
    
def criar_comentario(request,id):
    materia = Materia.objects.get(id=id)
    if request.method == 'POST':
        if materia:
            nome_usuario = request.POST.get('nome_usuario')
            comentario = request.POST.get('comentario')
            data_comentario = request.POST.get('data_comentario')
            
            Comentario.objects.create(pk_materia_id=id, nome_usuario=nome_usuario, comentario=comentario, data_comentario=data_comentario)
            return redirect('info_materia',id)
    else:
        return render(request, 'comentario.html',{'materia':materia})


def lista_favoritos(request, id):
    materia = Materia.objects.get(id=id)
    if materia:
        Favoritos.objects.create(materia_id=materia.id, usuario_id=request.user.id)
        return redirect('blog')
    else:
        return render(request, 'indx.html',{'materia':materia})


def exibir_favoritos(request, id):
    materia = Materia.objects.get(id=id)
    favoritos = Favoritos.objects.filter(materia=id)
    if favoritos:
        print("aqui",favoritos)
        return render(request, 'favoritos.html',{'favoritos':favoritos, 'materia':materia})
    else:
        return redirect('blog')