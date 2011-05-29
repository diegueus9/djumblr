# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    help = 'Import posts from tumblr'
    args = '<tumblr url>'
    requires_model_validation = True
    can_import_settings = True

    def handle(self, *args, **options):
        print 'working...'