# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Payment'
        db.create_table(u'paymaster_payment', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('payment_num', self.gf('django.db.models.fields.BigIntegerField')(default=0)),
            ('datetime', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('datetime_last_update', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('owner', self.gf('django.db.models.fields.related.ForeignKey')(related_name='paymaster_payment_owner', to=orm['auth.User'])),
            ('operation_amount', self.gf('django.db.models.fields.DecimalField')(max_digits=12, decimal_places=2)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('operation_status', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('ammount', self.gf('django.db.models.fields.DecimalField')(max_digits=12, decimal_places=2)),
            ('system_payment_id', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('payer_identifier', self.gf('django.db.models.fields.CharField')(default=' ', max_length=100)),
        ))
        db.send_create_signal(u'paymaster', ['Payment'])


    def backwards(self, orm):
        # Deleting model 'Payment'
        db.delete_table(u'paymaster_payment')


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
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'paymaster.payment': {
            'Meta': {'object_name': 'Payment'},
            'ammount': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '2'}),
            'datetime': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'datetime_last_update': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'operation_amount': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '2'}),
            'operation_status': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'paymaster_payment_owner'", 'to': u"orm['auth.User']"}),
            'payer_identifier': ('django.db.models.fields.CharField', [], {'default': "' '", 'max_length': '100'}),
            'payment_num': ('django.db.models.fields.BigIntegerField', [], {'default': '0'}),
            'system_payment_id': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['paymaster']