#! /usr/bin/env python
# -*- coding: utf-8 -*-
# шаблонный тег
from django import template
from django.template import Template
register = template.Library()


# шаблонный тег
@register.simple_tag(takes_context=True)
def editlink(context):
    return Template('<div><br/><b>шаблонный тег:</b> {{ username }}</div>').render(context)
    #return '123321'