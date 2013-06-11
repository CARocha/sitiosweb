from eventos.models import Eventos
from noticias.models import Noticias

def globales(request):
	evento = Eventos.objects.order_by('-id')[:3]
	noticia = Noticias.objects.order_by('-id')[:4]

	return {'eventos':evento, 'noticias':noticia}