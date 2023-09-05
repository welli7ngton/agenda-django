from django.contrib import admin
from contact.models import Contact, Category


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    # configurações de exibição da área administratica do django
    # lista os campos das tabelas do banco de dados
    list_display = (
        'id',
        'first_name',
        'last_name',
        'phone',
        'email',
        'category',
        'show',
    )

    # ordena os a exibição dos dados
    ordering = (
        '-id',
    )

    # faz buscas pelos campos definidos
    search_fields = (
        'id',
        'first_name',
        'last_name',
    )

    # quantidade de itens listados por página
    list_per_page = 10

    # quantidade de itens mostrados no "mostrar tudo"
    list_max_show_all = 200

    # deixa o campo de first name editável na área de pesquisa
    list_editable = 'show',


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )
