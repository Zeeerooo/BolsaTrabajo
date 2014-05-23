# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Offer'
        db.create_table(u'public_offer', (
            ('id', self.gf('django.db.models.fields.CharField')(default='77L`?r;}QhV=6?:)mG4o', max_length=20, primary_key=True)),
            ('long_description', self.gf('django.db.models.fields.CharField')(max_length=2000, blank=True)),
            ('short_description', self.gf('django.db.models.fields.CharField')(max_length=140, blank=True)),
            ('tecnologies', self.gf('django.db.models.fields.CharField')(max_length=500, blank=True)),
            ('date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('expire_date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('institution', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('responsable', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('mail', self.gf('django.db.models.fields.EmailField')(max_length=70, blank=True)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('length', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('work_direction', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
        ))
        db.send_create_signal(u'public', ['Offer'])

        # Adding M2M table for field offer_type on 'Offer'
        db.create_table(u'public_offer_offer_type', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('offer', models.ForeignKey(orm[u'public.offer'], null=False)),
            ('offer_type', models.ForeignKey(orm[u'public.offer_type'], null=False))
        ))
        db.create_unique(u'public_offer_offer_type', ['offer_id', 'offer_type_id'])

        # Adding model 'Offer_Type'
        db.create_table(u'public_offer_type', (
            ('id', self.gf('django.db.models.fields.IntegerField')(max_length=1, primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'public', ['Offer_Type'])


    def backwards(self, orm):
        
        # Deleting model 'Offer'
        db.delete_table(u'public_offer')

        # Removing M2M table for field offer_type on 'Offer'
        db.delete_table('public_offer_offer_type')

        # Deleting model 'Offer_Type'
        db.delete_table(u'public_offer_type')


    models = {
        u'public.offer': {
            'Meta': {'object_name': 'Offer'},
            'date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'expire_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'id': ('django.db.models.fields.CharField', [], {'default': "'77L`?r;}QhV=6?:)mG4o'", 'max_length': '20', 'primary_key': 'True'}),
            'institution': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'length': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'long_description': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'blank': 'True'}),
            'mail': ('django.db.models.fields.EmailField', [], {'max_length': '70', 'blank': 'True'}),
            'offer_type': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['public.Offer_Type']", 'null': 'True', 'blank': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'responsable': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'short_description': ('django.db.models.fields.CharField', [], {'max_length': '140', 'blank': 'True'}),
            'tecnologies': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'work_direction': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'})
        },
        u'public.offer_type': {
            'Meta': {'object_name': 'Offer_Type'},
            'id': ('django.db.models.fields.IntegerField', [], {'max_length': '1', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['public']
