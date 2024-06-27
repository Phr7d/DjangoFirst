from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from blog.models import Post
from django.utils import timezone
# Create your views here.

def blog_view(request):
    #Show posts from ordering time pulished date
    posts = Post.objects.filter(pulished_date__lte=timezone.now())
    context = {'postss': posts}
    return render(request,'blog/blog-home.html',context)

def blog_single(request):
    return render(request,'blog/blog-single.html')

def test_view(request,pid):
    #get post from slug
    posts = Post.objects.get(id = pid)
    #add to count view
    posts.counted_view = posts.counted_view + 1
    #Save counted view
    posts.save()
    context = {'postss': posts}
    return render(request,'website/test.html',context)