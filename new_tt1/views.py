#! /usr/bin/env python
# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, get_object_or_404, render, redirect
from .models import Presentation, RequestContent
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.conf import settings
from .forms import PresentationForm
from django.contrib import auth
from django.http import Http404
from django.db.models import get_model
from django.views.generic import ListView
from django.test.client import RequestFactory





def requestContetnView(ListView):
    querysets = RequestContent.objects.all().order_by('-date')[:10]
    return render_to_response('request.html', {'querysets': querysets})


def home(request):
    # Работаем с объектом
    queryset = Presentation.objects.all()
    for item in queryset:
        name = item.name  # выводим адрес
        surname = item.surname  # выводим город
        birthdate = item.birthdate  # выводим дату рождения
        bio = item.bio  # выводим инфо
        phone = item.phone  # выводим телефон
        skype = item.skype  # выводим skype
        photo = item.photo  # выводим фото

    # TEMPLATE_CONTEXT_PROCESSORS
    val1 = settings.MY_EMAIL
    val2 = settings.MY_NAME
    response_dict = RequestContext(request)
    # добавляем новое значение
    response_dict['some_var_only_in_this_view'] = 42

    tmp_dict = RequestContext(request)
    tmp_dict.update(response_dict)

    return render_to_response('index.html',
                              {'MY_EMAIL': val1, 'MY_NAME': val2, 'queryset': queryset, 'response_dict': response_dict,
                               'name': name, 'surname': surname, 'birthdate': birthdate, 'bio': bio, 'phone': phone,
                               'skype': skype, 'photo': photo, 'username': auth.get_user(request).username, })


def post_edit(request):
    instance = get_object_or_404(Presentation.objects.all())
    if request.method == "POST":
        form = PresentationForm(request.POST or None, request.FILES or None, instance=instance)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            #message.success()
            return HttpResponseRedirect('/')
    else:
        form = PresentationForm(instance=instance)
    return render(request, 'edit.html', {'form': form})







