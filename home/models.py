from django.db import models
from django.contrib.auth.models import User
import datetime


class Article(models.Model):
    
    title = models.CharField('Title', max_length = 100)
    content = models.TextField('Article content')
    create_date = models.DateTimeField('Created at', default = datetime.datetime.now())
    modify_date = models.DateTimeField('Last Modified', default = datetime.datetime.now())
    image_url = models.FileField('Image', upload_to = 'uploads/')
    published = models.BooleanField('Publushed?', default = False )
    featured = models.BooleanField('Featured?', default = False )
    
    # Relationship
    username = models.ForeignKey(User, on_delete = models.CASCADE)
    
    def __str__(self):
        return self.title
    
