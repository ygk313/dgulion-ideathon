from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Like, Comment
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.http import HttpResponse
import json
from django.template.loader import render_to_string

def main(request):
    posts = Post.objects.all()
    return render(request, 'main.html', {'posts':posts})

def create(request):
    user = request.user
    if user.is_anonymous:
        return redirect('account_login')

    if request.method=="POST":
        post = Post()
        post.title = request.POST['title']
        post.content = request.POST['content']
        post.user = user
        post.image = request.FILES.get('image')
        post.save()
        return redirect('homepage:detail', post.id)
    else:
        return render(request,'homepage/create.html')

def detail(request, pk):
    posts = get_object_or_404(Post, pk=pk)
    name = str(posts.image)[7:]
    return render(request, 'homepage/detail.html', {'posts':posts, 'name':name})

def delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('main')

def new_update(request, pk):
    post = get_object_or_404(Post, pk=pk)
    name = str(post.image)[7:]
    return render(request, 'homepage/update.html', {'post':post, 'name':name})

def update(request, pk):
    if request.method == "POST":
        post = get_object_or_404(Post, pk=pk)
        post.title = request.POST['title']
        post.content = request.POST['content']
        
        if request.FILES.get('image'):
            post.image = request.FILES.get('image')
        
        post.save()
        
        return redirect('homepage:detail', post.id)

def mylist(request):
    user = request.user
    posts = Post.objects.filter(user = user)
    return render(request, 'homepage/mylist.html', {'posts':posts})

def mylikes(request):
    user = request.user
    likes = Like.objects.filter(user = user)
    return render(request, 'homepage/mylikes.html', {'likes':likes})

def mycomments(request):
    user = request.user
    comments = Comment.objects.filter(users = user)
    return render(request, 'homepage/mycomments.html', {'comments': comments})


@require_POST
@login_required
def like_toggle(request, pk):
    post = get_object_or_404(Post, pk = pk)
    post_like, post_like_created = post.like_set.get_or_create(user=request.user)

    if not post_like_created:
        post_like.delete()
        result = "like_cancel"
    else:
        result = "like"

    context={
        'likes_counts':post.likes_counts,
        'result':result
    }
    
    return HttpResponse(json.dumps(context), content_type="application/json")

@login_required
@require_POST
def create_comment(request, pk):
    user = request.user
    if user.is_anonymous:
        return redirect('account_login')
    
    if request.method == "POST":
        post = get_object_or_404(Post, pk=pk)
        message = request.POST.get('message')
        comment = Comment.objects.create(users=user, post=post, message=message)

        return redirect('homepage:detail', post.pk )
    
    return render(request, 'main.html')

def delete_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    post_id = comment.post.id
    comment.delete()
    return redirect('homepage:detail', post_id)

def delete_image(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post.image != None:
        post.image = None
        post.save()
    return redirect('homepage:new_update', post.pk)