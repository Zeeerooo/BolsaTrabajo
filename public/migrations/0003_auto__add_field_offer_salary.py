# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Offer.salary'
        db.add_column(u'public_offer', 'salary',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=30, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Offer.salary'
        db.delete_column(u'public_offer', 'salary')


    models = {
        u'public.offer': {
            'Meta': {'object_name': 'Offer'},
            'date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'expire_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'id': ('django.db.models.fields.CharField', [], {'default': "'0$y\\x0b\\x0cVBs@tekRDRKzzdf'", 'max_length': '20', 'primary_key': 'True'}),
            'institution': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'length': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'long_description': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'blank': 'True'}),
            'mail': ('django.db.models.fields.EmailField', [], {'max_length': '70', 'blank': 'True'}),
            'offer_type': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['public.Offer_Type']", 'null': 'True', 'blank': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'responsable': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'salary': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'short_description': ('django.db.models.fields.CharField', [], {'max_length': '140', 'blank': 'True'}),
            'tecnologies': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'verified': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'work_direction': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'})
        },
        u'public.offer_type': {
            'Meta': {'object_name': 'Offer_Type'},
            'id': ('django.db.models.fields.IntegerField', [], {'max_length': '1', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['public']