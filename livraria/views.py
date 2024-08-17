from django.core.paginator import Paginator
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

def excluir_livro(request, livro_id):
    livro = get_object_or_404(Livro, pk=livro_id)

    if request.method == 'POST':
        livro.delete()
        return redirect('lista')
    
    return render(request, 'livraria/excluir_livro.html', {'livro': livro})

def detalhes_livro(request, livro_id):
    livro = get_object_or_404(Livro, pk=livro_id)
    return render(request, 'livraria/detalhes_livro.html', {'livro':livro})

def lista_livros(request):
    query = request.GET.get('q')
    ano = request.GET.get('ano')

    livros = Livro.objects.all()

    if query:
        livros = Livro.objects.filter(titulo__icontains=query) | Livro.objects.filter(autor__icontains=query)
    else:
        livros = Livro.objects.all()

    if ano:
        livros = livros.filter(ano_publicacao=ano)

    # Adicionando a paginação
    paginator = Paginator(livros, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'livraria/lista_livros.html', {'livros': livros})