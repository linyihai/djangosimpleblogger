from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponseRedirect
from blog.models import BlogPost, BlogPostForm

# Create your views here.


# def archive(request):
#     posts = BlogPost.objects.all()
#     return render(request,'archive.html',{'posts':posts})

archive = lambda request: render(request,'archive.html',{'posts':BlogPost.objects.all().order_by('-timestamp')[:10],'form':BlogPostForm})

def create_blogpost(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            # add timestamp
            post = form.save(commit=False)
            post.timestamp=datetime.now()
            post.save()
        return HttpResponseRedirect('/blog/')