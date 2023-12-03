from django.contrib import admin
from .models import Fotografia


class ListandoFotografias(admin.ModelAdmin):
    list_display = ("nome", "legenda", "publicado")
    list_display_links = ("nome",)
    search_fields = ("nome",)
    list_filter = ("categoria",)
    list_editable = ("publicado",)
    list_per_page = 10


admin.site.register(Fotografia, ListandoFotografias)
