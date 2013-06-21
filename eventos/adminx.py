from .models import Eventos
from multimedia.models import *
import xadmin
#from xadmin import views
from xadmin.layout import *

#from xadmin.plugins.inline import Inline
#from xadmin.plugins.batch import BatchChangeAction
from django.contrib.contenttypes import generic

class FotosAdmin(generic.GenericTabularInline):
    model = Fotos

class EventosAdmin(object):
    inlines = [FotosAdmin]

xadmin.site.register(Eventos, EventosAdmin)