from django.conf.urls import patterns, url
from noticias.views import NoticiasList, NoticiasDetailView

urlpatterns = patterns('noticias.views',
		url(r'^$', 'index', name='index'),
		url(r'^noticias/$', view=NoticiasList.as_view(), 
							name='noticias_lista'),
		url(r'^(?P<slug>[-_\w]+)/$', view=NoticiasDetailView.as_view(), 
									 name='noticias_detalle'),
	)