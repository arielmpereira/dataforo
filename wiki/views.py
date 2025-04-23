from django.shortcuts import render, get_object_or_404
from .models import Wiki

def lista_wiki(request):
    paginas = Wiki.objects.all().order_by('-actualizado')
    return render(request, 'wiki/lista.html', {'paginas': paginas})

def detalle_wiki(request, slug):
    pagina = get_object_or_404(Wiki, slug=slug)
    return render(request, 'wiki/detalle.html', {'pagina': pagina})

