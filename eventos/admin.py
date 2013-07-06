from django.contrib import admin
from .models import Eventos
from multimedia.models import *


class FotosAdmin(generic.GenericTabularInline):
    model = Fotos
    extra =1
    max_num = 1

class EventosAdmin(admin.ModelAdmin):

    # def save_model(self, request, obj, form, change):
    #     obj.autor = request.user
    #     obj.save()
        
    def queryset(self, request):
        qs = super(EventosAdmin, self).queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(autor=request.user)

    #exclude = ('autor',)
    inlines = [FotosAdmin]
    # fieldsets = (
    # ('nada', {
    #     'fields': ('titulo','fecha_inicio','fecha_finalizacion','descripcion','position','categoria')
    # }),
    # ('usuario', {
    #         'classes': ('usuarioforma',),
    #         'fields': ('autor',)
    #     }),
    # )

admin.site.register(Eventos, EventosAdmin)