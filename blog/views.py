from django.shortcuts import get_object_or_404,render
from blog.models import Blog
# Create your views here.

def home(request):
    blogs=Blog.objects.order_by("date")

    return render(request, "blog/home.html",{"blogs":blogs})

def detail(request,blog_id,ha_id=0):
    blog=get_object_or_404(Blog, pk=blog_id)

    return render(request, "blog/detail.html",{"id":blog_id,
                                               "ha_id":ha_id,
                                               "blog":blog
                                               
                                               
                                               })