#! /usr/bin/env python
# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
from datetime import datetime
from django.db.models import get_app, get_models

'''            Task 7

write this command in terminal:
./manage.py managecomand

'''

class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        self.stderr.write("error: ", ending='')

        f = open(datetime.now().strftime('%d_%m_%Y.log'), "a")
        # i have 1 model Presentation
        app = get_app('new_tt1')
        for Presentation in get_models(app):
            # count fields in model
            print "Presentation", len(Presentation._meta.fields)
            f.write('Presentation ' + str(len(Presentation._meta.fields)) + '\n')
        f.close()
        return