from django.contrib import admin
from .models import Materia


class materiaAdmin(admin.ModelAdmin):
    display_list = ['autor', 'titulo', 'descricao', 'data_publicacao', 'imagem']
    search_fields = ['autor', 'titulo']

admin.site.register(Materia, materiaAdmin)
