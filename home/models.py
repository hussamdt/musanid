from django.db import models
from django.contrib.auth.models import User

class Article(models.Model):
    
    title = models.CharField('Title', max_length = 100)
    content = models.TextField('Article content')
    create_date = models.DateTimeField('Created at',auto_now_add=True)
    modify_date = models.DateTimeField('Last Modified', auto_now=True)
    image_url = models.FileField('Image', upload_to = 'uploads/')
    published = models.BooleanField('Publushed?', default = False )
    featured = models.BooleanField('Featured?', default = False )
    
    # Relationship
    username = models.ForeignKey(User, on_delete = models.CASCADE)
    
    def __str__(self):
        return self.title
    
