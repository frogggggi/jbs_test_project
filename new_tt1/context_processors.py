#! /usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf import settings


def tmp_context_processor(request):
    # это процессор
    my_fungi = {
        'my_email': settings.MY_EMAIL,
        'my_name': settings.MY_NAME,
    }

    return my_fungi