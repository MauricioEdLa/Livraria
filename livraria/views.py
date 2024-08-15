from django.shortcuts import render, redirect, get_object_or_404
from .models import Livro
from .forms import LivroForm

def lista_livros(request):
    livros = Livro.objects.all()
    return render(request, 'livraria/lista_livros.html', {'livros': livros})

def adicionar_livro(request):
    if request.method == 'POST':
        form = LivroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_livros')
    else:
        form = LivroForm()
    return render(request, 'livraria/adicionar_livro.html', {'form': form})

def editar_livro(request, livro_id):
    livro = get_object_or_404(Livro, pk=livro_id)
    if request.method == 'POST':
        form = LivroForm(request.POST, instance=livro)
        if form.is_valid():
            form.save()
            return redirect('lista_livros')
    else:
        form = LivroForm(instance=livro)
    return render(request, 'livraria/editar_livro.html', {'form': form})