# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Catalog.seo_title'
   

        # Adding field 'Catalog.seo_content_hy'
        db.add_column(u'catalog_catalog', 'seo_content_hy',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Catalog.seo_content_ru'
        db.add_column(u'catalog_catalog', 'seo_content_ru',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Catalog.seo_content_en'
        db.add_column(u'catalog_catalog', 'seo_content_en',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Catalog.seo_keywords_hy'
        db.add_column(u'catalog_catalog', 'seo_keywords_hy',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Catalog.seo_keywords_ru'
        db.add_column(u'catalog_catalog', 'seo_keywords_ru',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Catalog.seo_keywords_en'
        db.add_column(u'catalog_catalog', 'seo_keywords_en',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Catalog.seo_title'
        db.add_column(u'catalog_catalog', 'seo_title',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)

        # Deleting field 'Catalog.seo_content_hy'
        db.delete_column(u'catalog_catalog', 'seo_content_hy')

        # Deleting field 'Catalog.seo_content_ru'
        db.delete_column(u'catalog_catalog', 'seo_content_ru')

        # Deleting field 'Catalog.seo_content_en'
        db.delete_column(u'catalog_catalog', 'seo_content_en')

        # Deleting field 'Catalog.seo_keywords_hy'
        db.delete_column(u'catalog_catalog', 'seo_keywords_hy')

        # Deleting field 'Catalog.seo_keywords_ru'
        db.delete_column(u'catalog_catalog', 'seo_keywords_ru')

        # Deleting field 'Catalog.seo_keywords_en'
        db.delete_column(u'catalog_catalog', 'seo_keywords_en')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'catalog.catalog': {
            'Meta': {'object_name': 'Catalog'},
            'category_type': ('django.db.models.fields.CharField', [], {'default': "'magazine'", 'max_length': '10'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            u'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'name_hy': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'name_ru': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'name_slug': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'original_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'blank': 'True', 'related_name': "'sub_category'", 'null': 'True', 'to': u"orm['catalog.Catalog']"}),
            'pub': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'seo_content': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'seo_content_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'seo_content_hy': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'seo_content_ru': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'seo_keywords': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'seo_keywords_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'seo_keywords_hy': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'seo_keywords_ru': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'sorting': ('django.db.models.fields.PositiveIntegerField', [], {}),
            u'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        u'catalog.currencyhistory': {
            'Meta': {'object_name': 'CurrencyHistory'},
            'date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'dram2usd': ('django.db.models.fields.DecimalField', [], {'max_digits': '8', 'decimal_places': '4'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'rub2dram': ('django.db.models.fields.DecimalField', [], {'max_digits': '8', 'decimal_places': '4'})
        },
        u'catalog.importlog': {
            'Meta': {'ordering': "('-id',)", 'object_name': 'ImportLog'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_imported': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'issue': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['catalog.Issue']"}),
            'journal': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['catalog.Journal']"})
        },
        u'catalog.issue': {
            'Meta': {'object_name': 'Issue'},
            'cover': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_archive': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_empty': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'journal': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['catalog.Journal']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'original_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'})
        },
        u'catalog.journal': {
            'Meta': {'object_name': 'Journal'},
            'category': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['catalog.Catalog']", 'symmetrical': 'False', 'blank': 'True'}),
            'count_for_pay': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'cover': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'max_length': '250', 'blank': 'True'}),
            'description_en': ('django.db.models.fields.TextField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'description_hy': ('django.db.models.fields.TextField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'description_ru': ('django.db.models.fields.TextField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'in_am': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'in_book': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'in_category': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'in_everyday': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'in_popular_pressa': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'in_pressa': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'journal_type': ('django.db.models.fields.CharField', [], {'default': "'magazine'", 'max_length': '10'}),
            'last_issue_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'name_hy': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'name_ru': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'name_slug': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'original_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '2'}),
            'price_dram': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '2'}),
            'price_usd': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '2'}),
            'recount': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'seo_content': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'seo_content_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'seo_content_hy': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'seo_content_ru': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'seo_keywords': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'seo_keywords_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'seo_keywords_hy': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'seo_keywords_ru': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'seo_title': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'seo_title_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'seo_title_hy': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'seo_title_ru': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        u'catalog.purchase': {
            'Meta': {'object_name': 'Purchase'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'issue': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['catalog.Issue']"}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '2'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['catalog']
