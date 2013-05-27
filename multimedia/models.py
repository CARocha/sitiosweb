#encoding: utf-8

from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from sorl.thumbnail import ImageField
from django.contrib.auth.models import User
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

	autor = models.ForeignKey(User)

	def __unicode__(self):
		return self.nombre
	class Meta:
		verbose_name_plural = "Fotos"

class Audio(models.Model):
	nombre = models.CharField(max_length=150)
	audio = models.FileField(upload_to=get_file_path, null=True, blank=True)
	tags_audio = TagAutocompleteField("Tags",help_text='Separar elementos con "," ', 
						              null=True, blank=True)

	def __unicode__(self):
		return self.nombre
	class Meta:
		verbose_name_plural = "Audios"

class Videos(models.Model):
	nombre= models.CharField(max_length=200, null=True, blank=True)
	url = models.URLField(null=True, blank=True)
	tags_video = TagAutocompleteField(help_text='Separar elementos con "," ', 
									  null=True, blank=True)

	def __unicode__(self):
		return self.nombre
	class Meta:
		verbose_name_plural = "Videos"
