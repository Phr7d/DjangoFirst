from django import template
from blog.models import Post, Category
from django.utils import timezone
from django.db.models import Q

register = template.Library()

@register.inclusion_tag('blog/blog-popular-post.html')
def blog_popular_post():
    posts = Post.objects.filter(Q(status=True) & Q(published_date__lte=timezone.now())).order_by('-published_date')[:3]
    return {'post': posts}

@register.inclusion_tag('blog/blog-post-category.html')
def postcategory():
    posts = Post.objects.filter(Q(status=True) & Q(published_date__lte=timezone.now()) )
    cat = Category.objects.all()
    cat_dict={}
    for name in cat:
        cat_dict[name] = posts.filter(category=name).count()
    return {'categories': cat_dict}

