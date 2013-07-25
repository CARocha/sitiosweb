from django.contrib import admin
from .models import Noticias, InicioTexto
from multimedia.models import *

from django.contrib.flatpages.admin import FlatPageAdmin
from django.contrib.flatpages.models import FlatPage

from django.contrib.flatpages.admin import FlatPageAdmin as FlatPageAdminOld
from django.contrib.flatpages.admin import FlatpageForm as FlatpageFormOld
 
from django import forms
from ckeditor.widgets import CKEditorWidget

class FotosAdmin(generic.GenericTabularInline):
    model = Fotos

class AdjuntoAdmin(generic.GenericTabularInline):
    model = Adjuntos

class NoticiasAdmin(admin.ModelAdmin):

    def queryset(self, request):
        qs = super(NoticiasAdmin, self).queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(autor=request.user)

    inlines = [FotosAdmin, AdjuntoAdmin]
    list_display = ['titulo','fecha','autor', 'get_tags']


class FlatpageForm(FlatpageFormOld):
    content = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = FlatPage
 
class FlatPageAdmin(FlatPageAdminOld):
    form = FlatpageForm

admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageAdmin)

admin.site.register(Noticias, NoticiasAdmin)
admin.site.register(InicioTexto)