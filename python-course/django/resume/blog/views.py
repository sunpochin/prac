from django.shortcuts import render, get_object_or_404
from .models import Blog

# Create your views here.


def all_blogs(request):
    temp = Blog.objects.order_by('-date')
    context = {
        'blogs': temp
    }
    return render(request, 'blog/all_blogs.html', context)


def blog_detail(request, blog_no):
    item = get_object_or_404(Blog, id=blog_no)
    context = {
        'blog': item
    }
    return render(request, 'blog/blog_detail.html', context)
