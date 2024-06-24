from django.db import models

# Create your models here.
class Post(models.Model):
    #image
    #author
    title = models.CharField(max_length=255)
    content = models.TextField()
    #tag
    #category
    counted_view = models.IntegerFeild(default=0)

