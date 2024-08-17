from django.urls import path
from .views import lista_livros, adicionar_livro, editar_livro, excluir_livro, detalhes_livro

urlpatterns = [
    path('livros/', lista_livros, name='lista_livros'),
    path('livros/adicionar/', adicionar_livro, name='adicionar_livro'),
    path('livros/editar/<int:livro_id>/', editar_livro, name='editar_livro'),
    path('livros/excluir/<int:livro_id>/', excluir_livro, name='excluir_livro'),
    path('livros/detalhes/<int:livro_id>/', detalhes_livro, name='detalhes_livro')
]