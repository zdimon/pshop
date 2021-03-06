# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Journal'
        db.create_table(u'catalog_journal', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=250, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(max_length=250, blank=True)),
            ('journal_type', self.gf('django.db.models.fields.CharField')(default='magazine', max_length=10)),
            ('price', self.gf('django.db.models.fields.DecimalField')(max_digits=12, decimal_places=2)),
        ))
        db.send_create_signal(u'catalog', ['Journal'])


    def backwards(self, orm):
        # Deleting model 'Journal'
        db.delete_table(u'catalog_journal')


    models = {
        u'catalog.catalog': {
            'Meta': {'object_name': 'Catalog'},
            'category_type': ('django.db.models.fields.CharField', [], {'default': "'magazine'", 'max_length': '10'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            u'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'name_slug': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'original_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'blank': 'True', 'related_name': "'sub_category'", 'null': 'True', 'to': u"orm['catalog.Catalog']"}),
            'pub': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            u'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        u'catalog.journal': {
            'Meta': {'object_name': 'Journal'},
            'description': ('django.db.models.fields.TextField', [], {'max_length': '250', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'journal_type': ('django.db.models.fields.CharField', [], {'default': "'magazine'", 'max_length': '10'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '2'})
        }
    }

    complete_apps = ['catalog']