from django.contrib import admin
from .models import Noticias
from multimedia.models import *

class FotosAdmin(generic.GenericTabularInline):
	model = Fotos

class NoticiasAdmin(admin.ModelAdmin):
	inlines = [FotosAdmin]


admin.site.register(Noticias, NoticiasAdmin)