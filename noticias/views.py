from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Noticias, InicioTexto
from multimedia.models import Videos, Audio
from eventos.models import Eventos
from publicaciones.models import Publicaciones
from .forms import ContactForm
from django.core.mail import send_mail
from django.http import HttpResponse
import json

def index(request, template='index.html'):
    #ultimas 3 noticias
    ultimas_noticias = Noticias.objects.order_by('-id')[0:3]
    #ultimas 4 noticias destacadas
    ultimas_destacadas = Noticias.objects.filter(destacada=True).order_by('-id')[0:4]
    #2 videos 
    ultimos_videos = Videos.objects.order_by('-id')[0:2]
    #2 eventos
    ultimos_eventos = Eventos.objects.order_by('-id')[0:2]
    #3 ultimas publicaciones
    ultimas_publicaciones = Publicaciones.objects.order_by('-id')[0:3]
    #4 ultimos audios
    ultimos_audios = Audio.objects.order_by('-id')[0:4]
    #testo al inicio de la pagina
    texto = InicioTexto.objects.all()
    
    return render(request, template, {'ultimas_noticias':ultimas_noticias,
                                       'ultimas_destacadas':ultimas_destacadas,
                                       'ultimos_videos':ultimos_videos,
                                       'ultimos_eventos':ultimos_eventos,
                                       'ultimas_publicaciones':ultimas_publicaciones,
                                       'ultimos_audios':ultimos_audios,
                                       'texto':texto})


class NoticiasList(ListView):
    model = Noticias
    paginate_by = 4

class NoticiasDetailView(DetailView):
    model = Noticias

def multimedia_publicacion(request, template='multimedia/multimedia_publi.html'):
  ultimas_publicaciones = Publicaciones.objects.order_by('-id')[0:5]
  ultimos_audios = Audio.objects.order_by('-id')[0:4]
  ultimos_videos = Videos.objects.order_by('-id')[0:4]

  return render(request, template, { 'ultimos_videos':ultimos_videos,
                                     'ultimas_publicaciones':ultimas_publicaciones,
                                     'ultimos_audios':ultimos_audios})

def filtro_categoria(request,categoria,template='noticias/noticias_list.html'):
    object_list = Noticias.objects.filter(categoria=categoria)
    return render(request, template, {'object_list':object_list})

def contacto(request, template='contacto.html'):
    form = ContactForm()
    texto2 = InicioTexto.objects.filter(id=2)
    return render(request, template, {'form': form,'texto2':texto2})

def contacto_ajax(request):
    if request.is_ajax():
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['asunto']
            message = form.cleaned_data['mensaje']
            sender = form.cleaned_data['correo']

            recipients = ['info@asonvihsida.org.ni',
                          'crocha09.09@gmail.com']

            send_mail(subject, message, sender, recipients)
            return HttpResponse( json.dumps( 'exito' ), mimetype='application/json' )
        else:
            return HttpResponse( json.dumps( 'falso' ), mimetype='application/json' )