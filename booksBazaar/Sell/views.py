from .forms import PostForm
from django.shortcuts import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404,redirect
from .models import Post


def post_list(request):
    posts = Post.objects.all()
    return render(request,'Sell/index.html',{'posts': posts})
		

def post_detail(request, id=None):
    post = get_object_or_404(Post,id=id)
    return render(request,'Sell/detail.html',{'post': post})

def post_create(request):
    form=PostForm(request.POST or None)
    if form.is_valid():
        post=form.save(commit=False)
        post.save()
        return HttpResponseRedirect(post.get_absolute_url())
        
    
        
    context={"form":form,}
    return render(request,"Sell/post_form.html",context)

def post_update(request,id=None):
    post = get_object_or_404(Post,id=id)
    form=PostForm(request.POST or None,instance=post)
    if form.is_valid():
        post=form.save(commit=False)
        post.save()
        return HttpResponseRedirect(post.get_absolute_url())
    
        
    context={"form":form,}
    return render(request,"Sell/post_form.html",context)






def post_delete(request,id=None):
    post = get_object_or_404(Post,id=id)
    post.delete()
    return redirect('Sell:post_list')
    
        
    context={"form":form,}
    return render(request,"Sell/post_form.html",context)