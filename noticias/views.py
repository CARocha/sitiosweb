from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Noticias


def index(request, template='index.html'):
	hola = "hola con render"
	noticias = Noticias.objects.all()
	return render(request, template, {'hola':hola,'noticias':noticias})


class NoticiasList(ListView):
	model = Noticias

class NoticiasDetailView(DetailView):

    model = Noticias

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(NoticiasDetailView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['noticias_list'] = Noticias.objects.all()
        return context