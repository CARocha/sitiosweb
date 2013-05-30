from django.conf.urls import patterns, url
from noticias.views import NoticiasList, NoticiasDetailView

urlpatterns = patterns('noticias.views',
		url(r'^$', 'index', name='index'),
		url(r'^noticias/$', NoticiasList.as_view()),
		url(r'^(?P<slug>[-_\w]+)/$', NoticiasDetailView.as_view(), name='noticias_detalle'),
	)