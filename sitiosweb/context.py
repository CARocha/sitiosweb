from eventos.models import Eventos
from noticias.models import Noticias, InicioTexto

def globales(request):
	evento = Eventos.objects.order_by('-id')[:3]
	noticia = Noticias.objects.order_by('-id')[:4]
	texto_contacto = InicioTexto.objects.filter(id=3)

	return {'eventos':evento, 'noticias':noticia, 'texto_contacto':texto_contacto}