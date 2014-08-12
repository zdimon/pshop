# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding M2M table for field category on 'Journal'
        m2m_table_name = db.shorten_name(u'catalog_journal_category')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('journal', models.ForeignKey(orm[u'catalog.journal'], null=False)),
            ('catalog', models.ForeignKey(orm[u'catalog.catalog'], null=False))
        ))
        db.create_unique(m2m_table_name, ['journal_id', 'catalog_id'])


    def backwards(self, orm):
        # Removing M2M table for field category on 'Journal'
        db.delete_table(db.shorten_name(u'catalog_journal_category'))


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
        u'catalog.issue': {
            'Meta': {'object_name': 'Issue'},
            'cover': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'journal': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['catalog.Journal']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'})
        },
        u'catalog.journal': {
            'Meta': {'object_name': 'Journal'},
            'category': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['catalog.Catalog']", 'symmetrical': 'False', 'blank': 'True'}),
            'cover': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'max_length': '250', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'journal_type': ('django.db.models.fields.CharField', [], {'default': "'magazine'", 'max_length': '10'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'name_slug': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'original_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '2'})
        }
    }

    complete_apps = ['catalog']