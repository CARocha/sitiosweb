#encoding: utf-8

from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from sorl.thumbnail import ImageField
from sitiosweb.utils import get_file_path
from tagging_autocomplete.models import TagAutocompleteField

# Create your models here.
# 
class Fotos(models.Model):
	nombre = models.CharField(max_length=150)
	imagen = ImageField(upload_to=get_file_path, blank=True, null=True)
	tags_fotos = TagAutocompleteField("Tags",help_text='Separar elementos con "," ', 
						         null=True, blank=True)

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = generic.GenericForeignKey('content_type', 'object_id')

	fileDir = 'fotos/'

	def __unicode__(self):
		return self.nombre
	class Meta:
		verbose_name_plural = "Fotos"

class Audio(models.Model):
	nombre = models.CharField(max_length=150)
	audio = models.FileField(upload_to=get_file_path, null=True, blank=True)
	tags_audio = TagAutocompleteField("Tags",help_text='Separar elementos con "," ', 
						              null=True, blank=True)
	fileDir = 'audios/'
	
	def __unicode__(self):
		return self.nombre
	class Meta:
		verbose_name_plural = "Audios"
		ordering = ('-id',)

class Videos(models.Model):
	nombre= models.CharField(max_length=200, null=True, blank=True)
	url = models.URLField(null=True, blank=True)
	tags_video = TagAutocompleteField(help_text='Separar elementos con "," ', 
									  null=True, blank=True)

	def __unicode__(self):
		return self.nombre
	class Meta:
		verbose_name_plural = "Videos"
		ordering = ('-id',)

class Adjuntos(models.Model):
	nombre = models.CharField(max_length=150)
	archivo = models.FileField(upload_to=get_file_path, blank=True, null=True)

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = generic.GenericForeignKey('content_type', 'object_id')

	fileDir = 'adjuntos/'

	def __unicode__(self):
		return self.nombre
	class Meta:
		verbose_name_plural = "Adjuntos"
