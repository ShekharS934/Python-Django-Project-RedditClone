from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Post

# Create your views here.
@login_required
def create(request):
    if request.method=='POST':
        if request.POST['Title'] and request.POST['Url']:
            post=Post()
            post.title= request.POST['Title']
            if request.POST['Url'].startswith('http://') or request.POST['Url'].startswith('https://'):
                post.url= request.POST['Url']
            else:
                post.url= 'http://' + request.POST['Url']
            post.pub_date = timezone.datetime.now()
            post.author= request.user
            post.save()
            return redirect('home')
        else:
            return render(request, 'posts/create.html', {'error':'ERROR, You must include a title and a URL to create a Post'})
        
    else:
        return render(request, 'posts/create.html')
    
    
    
def home(request):
    posts= Post.objects.order_by('-votes_total') 
    return render(request, 'posts/home.html', {'posts':posts})


def upvote(request, pk):
    if request.method=='POST':
        post= Post.objects.get(pk=pk)
        post.votes_total +=1
        post.save()
        return redirect('home')


def downvote(request, pk):
    if request.method=='POST':
        post= Post.objects.get(pk=pk)
        post.votes_total -=1
        post.save()
        return redirect('home')
    
    
def userposts(request, fk):
    posts= Post.objects.filter(author__id=fk).order_by('-votes_total')
    return render(request, 'posts/userposts.html', {'posts':posts})
        