from django.shortcuts import render, get_object_or_404
from .models import Fotografia


def index(request):
    fotografias = Fotografia.objects.order_by("data_fotografia").filter(publicado=True)
    return render(request, 'galeria/index.html', {"cards": fotografias})


def imagem(request, id):
    fotografia = get_object_or_404(Fotografia, pk=id)
    return render(request, 'galeria/imagem.html', {"fotografia": fotografia})


def buscar(request):
    fotografias = Fotografia.objects.order_by("data_fotografia").filter(publicado=True)

    if 'buscar' in request.GET:
        nome_buscar = request.GET['buscar']
        if nome_buscar:
            fotografias = fotografias.filter(nome__icontains=nome_buscar)

    return render(request, 'galeria/buscar.html', {"cards": fotografias})
