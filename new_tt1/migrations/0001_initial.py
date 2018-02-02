# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Presentation'
        db.create_table(u'new_tt1_presentation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('surname', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('birthdate', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('bio', self.gf('django.db.models.fields.TextField')(null=True)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=50, null=True)),
            ('skype', self.gf('django.db.models.fields.CharField')(max_length=50, null=True)),
            ('photo', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal(u'new_tt1', ['Presentation'])


    def backwards(self, orm):
        # Deleting model 'Presentation'
        db.delete_table(u'new_tt1_presentation')


    models = {
        u'new_tt1.presentation': {
            'Meta': {'object_name': 'Presentation'},
            'bio': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'birthdate': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'skype': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'surname': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['new_tt1']