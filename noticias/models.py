#encoding: utf-8

from django.db import models
from ckeditor.fields import RichTextField
from django.template.defaultfilters import slugify
from multimedia.models import Fotos
from django.contrib.auth.models import User
from django.contrib.contenttypes import generic
from django.core.urlresolvers import reverse
from tagging.models import Tag
from tagging_autocomplete.models import TagAutocompleteField

# Create your models here.
class Noticias(models.Model):
    titulo = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200,editable=False)
    fecha = models.DateField()
    descripcion = RichTextField('Descripción')
    fotos = generic.GenericRelation(Fotos)
    categoria= TagAutocompleteField(help_text='Separar elementos con "," ', 
                                    null=True, blank=True)
    destacada = models.BooleanField()

    autor = models.ForeignKey(User)

    def save(self, *args, **kwargs):
        self.slug = (slugify(self.titulo))
        super(Noticias, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('noticias_detalle', kwargs={'slug': self.slug})

    def get_tags(self):
        return Tag.objects.get_for_object(self)

    class Meta:
        verbose_name = 'Noticia'
        verbose_name_plural = 'Noticias'

    def __unicode__(self):
        return u'%s' % self.titulo
