# -*- coding: utf-8 -*-
import getpass
from copy import copy

from tumblr import Api
from dateutil import parser

from django.core.management.base import BaseCommand, CommandError
from django.db.models import get_model

def translate_dict(post):
    data = {}
    for key, value in post.items():
        key = key.replace('-', '_')
        if key == 'id':
            key = 'tumblr_id'
        elif key in ['date', 'date_gmt']:
            value = parser.parse(value)
        elif key in ['tags', 'photos']:
            key = None
        if key is not None:
            data[key] = value
    return data

def _(post_data):
    photo_model = get_model('djumblr', 'PhotoPost')
    video_model = get_model('djumblr', 'VideoPost')
    text_model = get_model('djumblr', 'TextPost')
    link_model = get_model('djumblr', 'LinkPost')
    data = translate_dict(copy(post_data))
    if data['type'] == 'photo':
        post_instance = photo_model(**data)
    elif data['type'] == 'video':
        post_instance = video_model(**data)
    elif data['type'] == 'regular':
        post_instance = text_model(**data)
    elif data['type'] == 'link':
        post_instance = link_model(**data)
    else:
        print post_data
    post_instance.save()

class Command(BaseCommand):
    help = 'Import posts from tumblr'
    args = '<tumblr url>'
    requires_model_validation = True
    can_import_settings = True

    def handle(self, *args, **options):
        tumblr_model = get_model('djumblr', 'Tumblr')
        
        tumblr_name = 'diegueus9'
        tumblr_email = 'diegueus9@gmail.com'
        print 'working...'
        tumblr_api = Api(tumblr_name, tumblr_email, getpass.getpass('Your tumblr password:'))
        
        t, created = tumblr_model.objects.get_or_create(name=tumblr_name, email=tumblr_email)
        tumblr_response = tumblr_api.read()
        for post in tumblr_response:
            _(post)
            #try:
                #_(post)
            #except:
                #print post
                #break
                