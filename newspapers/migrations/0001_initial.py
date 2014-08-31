# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Newspaper'
        db.create_table(u'newspapers_newspaper', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('contact_name', self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True)),
            ('contact_phone', self.gf('django.db.models.fields.CharField')(max_length=15, null=True, blank=True)),
            ('contact_email', self.gf('django.db.models.fields.EmailField')(max_length=75, null=True, blank=True)),
        ))
        db.send_create_signal(u'newspapers', ['Newspaper'])


    def backwards(self, orm):
        # Deleting model 'Newspaper'
        db.delete_table(u'newspapers_newspaper')


    models = {
        u'newspapers.newspaper': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Newspaper'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'contact_email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'contact_name': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'contact_phone': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '32'})
        }
    }

    complete_apps = ['newspapers']