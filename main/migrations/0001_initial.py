# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Catalog'
        db.create_table(u'main_catalog', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('pub', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=250, blank=True)),
        ))
        db.send_create_signal(u'main', ['Catalog'])


    def backwards(self, orm):
        # Deleting model 'Catalog'
        db.delete_table(u'main_catalog')


    models = {
        u'main.catalog': {
            'Meta': {'object_name': 'Catalog'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'pub': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        }
    }

    complete_apps = ['main']