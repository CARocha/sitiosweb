from django.conf.urls import patterns, url
from noticias.views import NoticiasList, NoticiasDetailView

urlpatterns = patterns('noticias.views',
    url(r'^lista/$', view=NoticiasList.as_view(), 
                     name='noticias_lista'),
        
    url(r'^(?P<slug>[-_\w]+)/$', view=NoticiasDetailView.as_view(), 
                                 name='noticias_detalle'),
    url(r'^categoria/(?P<categoria>[-_\w]+)/$', 'filtro_categoria', 
                                 name='noticias_categoria'),
        
    )