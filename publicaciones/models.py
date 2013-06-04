#encoding: utf-8

from django.db import models
from ckeditor.fields import RichTextField
from django.template.defaultfilters import slugify
from sitiosweb.utils import get_file_path
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from tagging_autocomplete.models import TagAutocompleteField

# Create your models here.
class Publicaciones(models.Model):
    titulo = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200,editable=False)
    fecha = models.DateField('Fecha de publicación')
    descripcion = RichTextField('Descripción')
    adjunto = models.FileField(upload_to=get_file_path, null=True, blank=True)
    categoria= TagAutocompleteField(help_text='Separar elementos con "," ', 
                                    null=True, blank=True)

    fileDir = 'publicaciones/'

    autor = models.ForeignKey(User)

    def save(self, *args, **kwargs):
        self.slug = (slugify(self.titulo))
        super(Publicaciones, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('publicaciones_detalles', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = u'Publicacion'
        verbose_name_plural = 'Publicaciones'

    def __unicode__(self):
        return u'%s' % self.titulo
