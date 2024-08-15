from django.contrib import admin
from .models import Livro

@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'ano_publicacao', 'isbn')
    search_fields = ('titulo', 'autor', 'isbn')