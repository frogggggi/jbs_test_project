#! /usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from new_tt1 import views


#enable admin
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^requests/$', views.requestContetnView, name='request'),
    url(r'^edit/$', views.post_edit, name='post_edit'),
    url(r'^auth/', include('loginsys.urls')),
    url(r'^$', views.home, name='home'),
)



if settings.DEBUG:
    if settings.MEDIA_ROOT:
        urlpatterns += static(settings.MEDIA_URL,
            document_root=settings.MEDIA_ROOT)
# Эта строка опциональна и будет добавлять url'ы только при DEBUG = True
urlpatterns += staticfiles_urlpatterns()