from django.contrib import admin
from .models import Materia, Comentario, Favoritos


class materiaAdmin(admin.ModelAdmin):
    display_list = ['autor', 'titulo', 'descricao', 'categoria', 'data_publicacao', 'imagem']
    search_fields = ['autor', 'titulo', 'categoria']

admin.site.register(Materia, materiaAdmin)
admin.site.register(Comentario)
admin.site.register(Favoritos)
