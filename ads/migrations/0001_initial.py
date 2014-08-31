# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Ad'
        db.create_table(u'ads_ad', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('start_date', self.gf('django.db.models.fields.DateField')()),
            ('end_date', self.gf('django.db.models.fields.DateField')()),
            ('cost', self.gf('django.db.models.fields.DecimalField')(max_digits=6, decimal_places=2)),
            ('client_company', self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True)),
            ('client_contact', self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True)),
            ('client_phone', self.gf('django.db.models.fields.CharField')(max_length=15, null=True, blank=True)),
            ('client_email', self.gf('django.db.models.fields.EmailField')(max_length=75, null=True, blank=True)),
        ))
        db.send_create_signal(u'ads', ['Ad'])

        # Adding M2M table for field newspaper on 'Ad'
        m2m_table_name = db.shorten_name(u'ads_ad_newspaper')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('ad', models.ForeignKey(orm[u'ads.ad'], null=False)),
            ('newspaper', models.ForeignKey(orm[u'newspapers.newspaper'], null=False))
        ))
        db.create_unique(m2m_table_name, ['ad_id', 'newspaper_id'])


    def backwards(self, orm):
        # Deleting model 'Ad'
        db.delete_table(u'ads_ad')

        # Removing M2M table for field newspaper on 'Ad'
        db.delete_table(db.shorten_name(u'ads_ad_newspaper'))


    models = {
        u'ads.ad': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Ad'},
            'client_company': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'client_contact': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'client_email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'client_phone': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'cost': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '2'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
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