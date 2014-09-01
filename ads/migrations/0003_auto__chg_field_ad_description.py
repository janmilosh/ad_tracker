# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Ad.description'
        db.alter_column(u'ads_ad', 'description', self.gf('django.db.models.fields.CharField')(max_length=64))

    def backwards(self, orm):

        # Changing field 'Ad.description'
        db.alter_column(u'ads_ad', 'description', self.gf('django.db.models.fields.CharField')(max_length=32))

    models = {
        u'ads.ad': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Ad'},
            'client_company': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'client_contact': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'client_email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'client_phone': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'end_date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'newspaper': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['newspapers.Newspaper']", 'symmetrical': 'False'}),
            'start_date': ('django.db.models.fields.DateField', [], {})
        },
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

    complete_apps = ['ads']