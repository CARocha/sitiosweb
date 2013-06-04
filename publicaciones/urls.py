from django.conf.urls import patterns, url
from django.views.generic import ListView, DetailView
from .models import Publicaciones

urlpatterns = patterns('',
        url(r'^lista/$',  ListView.as_view(model=Publicaciones,
                                                               queryset=Publicaciones.objects.all(),
                                                               paginate_by=5), 
                                                               name='publicaciones_lista'),
        
        url(r'^(?P<slug>[-_\w]+)/$', DetailView.as_view(model=Publicaciones,
                                                                                            queryset=Publicaciones.objects.all(),
                                                                                            ), 
                                                                                            name='publicaciones_detalles'),
    )