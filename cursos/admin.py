from django.contrib import admin
from .models import Categoria, Curso


# Register your models here.
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome_categoria', 'slug')
    list_filter = ['nome_categoria']
    list_display_links = ['nome_categoria']
    prepopulated_fields = {"slug": ("nome_categoria",)}


admin.site.register(Categoria, CategoriaAdmin)


class CursoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome_curso', 'publicado')
    list_display_links = ('id', 'nome_curso')
    search_fields = ['nome_curso']
    list_editable = ['publicado']
    prepopulated_fields = {"slug": ("nome_curso",)}


admin.site.register(Curso, CursoAdmin)
