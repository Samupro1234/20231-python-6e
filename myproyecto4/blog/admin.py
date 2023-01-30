
from django.contrib import admin
from blog.models import usuario, visitante, guia, sitio
# Register your models here.()min

class usuarioAdmin(admin.ModelAdmin):
    list_display = ('nombres', 'apellidos')

admin.site.register(usuario,usuarioAdmin)
admin.site.register(visitante)
admin.site.register(guia)
admin.site.register(sitio)

