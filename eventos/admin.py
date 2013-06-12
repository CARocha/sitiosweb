from django.contrib import admin
from .models import Eventos
from multimedia.models import *

class FotosAdmin(generic.GenericTabularInline):
	model = Fotos

class EventosAdmin(admin.ModelAdmin):
	inlines = [FotosAdmin]

admin.site.register(Eventos, EventosAdmin)