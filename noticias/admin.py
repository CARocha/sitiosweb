from django.contrib import admin
from .models import Noticias
from multimedia.models import *

from django.contrib.flatpages.admin import FlatPageAdmin
from django.contrib.flatpages.models import FlatPage

from django.contrib.flatpages.admin import FlatPageAdmin as FlatPageAdminOld
from django.contrib.flatpages.admin import FlatpageForm as FlatpageFormOld
 
from django import forms
from ckeditor.widgets import CKEditorWidget

class FotosAdmin(generic.GenericTabularInline):
	model = Fotos

class NoticiasAdmin(admin.ModelAdmin):
	inlines = [FotosAdmin]
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