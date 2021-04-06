from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Curso, Categoria


# Create your views here.

def index(request):
    lista_cursos = Curso.objects.filter(publicado=True)
    lista_categorias = Categoria.objects.all()

    dados = {
        'cursos': lista_cursos,
        'categorias': lista_categorias

    }
    return render(request, 'index.html', dados)


def curso_detalhes(request, slug):
    curso = Curso.objects.get(slug=slug)

    dados = {

        'curso': curso
    }
    return render(request, 'curso.html', dados)


def lista_cursos_categoria(request, slug):
    categoria = get_object_or_404(Categoria, slug=slug)
    curso = Curso.objects.filter(categoria=categoria)

    dados = {

        'categorias': categoria,
        'cursos': curso
    }
    return render(request, 'categoria.html', dados)


def sobre(request):
    return render(request, 'sobre.html')


def contato(request):
    return render(request, 'contato.html')
