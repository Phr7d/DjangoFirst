from django import template
from blog.models import Post, Category
from django.utils import timezone
from django.db.models import Q

register = template.Library()

@register.inclusion_tag('website/latest-blog.html')
def latestPosts():
    posts = Post.objects.filter(Q(status=True) & Q(published_date__lte=timezone.now())).order_by('-published_date')[:6]
    return {'posts': posts}