from django.shortcuts import render, get_object_or_404, redirect
from apps.galeria.models import Fotografia
from django.contrib import messages


def index(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não está logado!')
        return redirect('login')

    fotografias = Fotografia.objects.order_by("data_fotografia").filter(publicado=True)
    return render(request, 'galeria/index.html', {"cards": fotografias})


def imagem(request, id):
    fotografia = get_object_or_404(Fotografia, pk=id)
    return render(request, 'galeria/imagem.html', {"fotografia": fotografia})


def buscar(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não está logado!')
        return redirect('login')
    
    fotografias = Fotografia.objects.order_by("data_fotografia").filter(publicado=True)

    if 'buscar' in request.GET:
        nome_buscar = request.GET['buscar']
        if nome_buscar:
            fotografias = fotografias.filter(nome__icontains=nome_buscar)

    return render(request, 'galeria/buscar.html', {"cards": fotografias})
