# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Fotos'
        db.create_table(u'multimedia_fotos', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('imagen', self.gf('sorl.thumbnail.fields.ImageField')(max_length=100, null=True, blank=True)),
            ('tags_fotos', self.gf('tagging_autocomplete.models.TagAutocompleteField')(null=True)),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contenttypes.ContentType'])),
            ('object_id', self.gf('django.db.models.fields.PositiveIntegerField')()),
        ))
        db.send_create_signal(u'multimedia', ['Fotos'])

        # Adding model 'Audio'
        db.create_table(u'multimedia_audio', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('audio', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('tags_audio', self.gf('tagging_autocomplete.models.TagAutocompleteField')(null=True)),
        ))
        db.send_create_signal(u'multimedia', ['Audio'])

        # Adding model 'Videos'
        db.create_table(u'multimedia_videos', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('tags_video', self.gf('tagging_autocomplete.models.TagAutocompleteField')(null=True)),
        ))
        db.send_create_signal(u'multimedia', ['Videos'])


    def backwards(self, orm):
        # Deleting model 'Fotos'
        db.delete_table(u'multimedia_fotos')

        # Deleting model 'Audio'
        db.delete_table(u'multimedia_audio')

        # Deleting model 'Videos'
        db.delete_table(u'multimedia_videos')


    models = {
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'multimedia.audio': {
            'Meta': {'object_name': 'Audio'},
            'audio': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'tags_audio': ('tagging_autocomplete.models.TagAutocompleteField', [], {'null': 'True'})
        },
        u'multimedia.fotos': {
            'Meta': {'object_name': 'Fotos'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagen': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'tags_fotos': ('tagging_autocomplete.models.TagAutocompleteField', [], {'null': 'True'})
        },
        u'multimedia.videos': {
            'Meta': {'object_name': 'Videos'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'tags_video': ('tagging_autocomplete.models.TagAutocompleteField', [], {'null': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['multimedia']