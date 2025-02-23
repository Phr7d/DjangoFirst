from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

# Create your models here.
class Post(models.Model):
    image = models.ImageField(upload_to='blog/images/', default='blog/images/default.jpg')
    favimage = models.ImageField(upload_to='blog/images/', default='blog/images/default.jpg')
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    #tag
    category = models.ManyToManyField(Category)
    counted_view = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    published_date = models.DateTimeField(null=True)
    created_date = models.DateTimeField(auto_now_add = True)
    updated_date = models.DateTimeField(auto_now = True)

    def Meta():
        ordering = ['-created_date']
    #on admin panel show title instead of object number
    def __str__(self):
        return self.title
