from django.db import models

class Tumblr(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()

class Tag(models.Model):
    name = models.CharField(max_length=255)

class TagInTumblr(models.Model):
    tag = models.ForeignKey(Tag)
    tumblr = models.ForeignKey(Tumblr)

class Post(models.Model):
    tumblr_id = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    format = models.CharField(max_length=255)
    
    reblog_key = models.CharField(max_length=255)

    feed_item = models.URLField(verify_exists=False, blank=True, null=True)
    from_feed_id = models.CharField(max_length=255, blank=True, null=True)

    mobile = models.IntegerField() # i think this is a boolean
    bookmarklet = models.IntegerField() # i dont knoe what is this but i suspect is a boolean

    unix_timestamp = models.IntegerField()
    date = models.DateTimeField()
    date_gmt = models.DateTimeField()

    url = models.URLField(verify_exists=False)
    slug = models.SlugField()
    url_with_slug = models.URLField(verify_exists=False)

class PhotoPost(Post):
    photo_caption = models.TextField(blank=True, null=True)
    photo_link_url = models.URLField(verify_exists=False)
    #tags = models.ManyToManyField(Tag)
    #photos = models.ManyToMany... # i dont know what is this
    
    height = models.IntegerField()
    width = models.IntegerField()

    photo_url_75 = models.URLField(verify_exists=False)
    photo_url_100 = models.URLField(verify_exists=False)
    photo_url_250 = models.URLField(verify_exists=False)
    photo_url_400 = models.URLField(verify_exists=False)
    photo_url_500 = models.URLField(verify_exists=False)
    photo_url_1280 = models.URLField(verify_exists=False)
    
class VideoPost(Post):
    video_caption = models.TextField(blank=True, null=True)
    video_source = models.URLField(verify_exists=False)
    video_player = models.TextField()
    video_player_250 = models.TextField()
    video_player_500 = models.TextField()

class TextPost(Post):
    regular_body = models.TextField()
    regular_title = models.CharField(max_length=255, blank=True, null=True)

class LinkPost(Post):
    link_url = models.URLField(verify_exists=False)
    link_description = models.TextField()
    link_text = models.CharField(max_length=255, blank=True, null=True)



    
    
