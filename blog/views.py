from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from blog.models import Post
from django.utils import timezone
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.

def blog_view(request,**kwargs):
    #Show posts from ordering time published date
    posts = Post.objects.filter(Q(status=True) & Q(published_date__lte=timezone.now())).order_by('-published_date')
    if kwargs.get('cat_name'):
        posts = posts.filter(category__name=kwargs['cat_name'])
    if kwargs.get('author_username'):
        posts = posts.filter(author__username=kwargs['author_username'])
    
    posts = Paginator(posts, 2)
    try:
        pageNum = request.GET.get('page')
        posts = posts.get_page(pageNum)
    except PageNotAnInteger:
        posts = post.page(1)
    except EmptyPage:
        posts = post.page(post.num_pages)
    context = {'postss': posts}
    return render(request,'blog/blog-home.html',context)



def blog_single(request,pid):
    try:
        posts = Post.objects.filter(Q(status=True) & Q(id=pid) & Q(published_date__lte=timezone.now())).get()
        context = {'post': posts}
        try:
            nextPost = Post.objects.filter(Q(status=True) & Q(published_date__lte=timezone.now()) & Q(id__gt=pid))[:1].get()
            context['nextPost'] = nextPost
        except:
            context['nextPost'] = 'End'
        try:
            prePost = Post.objects.filter(Q(status=True) & Q(published_date__lte=timezone.now()) & Q(id__lt=pid)).latest('id')
            context['prePost'] = prePost
        except :
            context['prePost'] = 'First'
        #get post from slug
        posts = Post.objects.get(id = pid)
        #add to count view
        posts.counted_view = posts.counted_view + 1
        #Save counted view
        posts.save()
        return render(request,'blog/blog-single.html',context)
    except:
        posts = get_object_or_404(Post,pk=0)



def search_view(request):
    # print(request.__dict__)
    posts = Post.objects.filter(Q(status=True) & Q(published_date__lte=timezone.now()))
    if request.method == 'GET':
        if s := request.GET.get('s'):
            print(s)
            posts = posts.filter(content__contains=s) 
    context = {'postss': posts}
    return render(request,'blog/blog-home.html',context)

