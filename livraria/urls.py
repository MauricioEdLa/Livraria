from django.urls import path
from .views import lista_livros, adicionar_livro, editar_livro

urlpatterns = [
    path('livros/', lista_livros, name='lista_livros'),
    path('livros/adicionar/', adicionar_livro, name='adicionar_livro'),
    path('livros/editar/<int:livro_id>', editar_livro, name='editar_livro'),
]