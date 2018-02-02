#! /usr/bin/env python
# -*- coding: utf-8 -*-
from django.forms import ModelForm, Textarea
from django import forms
from .models import Presentation
from widgets import JQueryUIDatePickerWidget as DateWidget
from django.db import models

from django.contrib.admin.widgets import AdminDateWidget
from django.forms.fields import DateField



class PresentationForm(ModelForm):
    birthdate = DateField(widget=AdminDateWidget)
    #birthdate = forms.DateTimeField(
    #    input_formats=['%Y-%m-%d'],
    #    label='Дата рождения',
    #    widget=AdminDateWidget,
    #    # widget=forms.CalendarInput,
    #)
    class Meta:
        model = Presentation
        fields = ('name', 'surname', 'birthdate', 'bio', 'phone', 'skype', 'photo',)
        widgets = {
            'birthdate': DateWidget
        }

    def __init__(self, *args, **kwargs):
        super(PresentationForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['class'] = 'form-control input-md'
        self.fields['surname'].widget.attrs['class'] = 'form-control input-md'
        self.fields['phone'].widget.attrs['class'] = 'form-control input-md'
        self.fields['skype'].widget.attrs['class'] = 'form-control input-md'
        #self.fields['birthdate'].widget.attrs['class'] = 'form-control'
        self.fields['photo'].widget.attrs['class'] = 'input-file'
        self.fields['bio'].widget.attrs['class'] = 'form-control'
        #self.fields['photo'].widget = CharField(attrs={
        #    'class': 'form-control',
        #    'type': 'file'})
