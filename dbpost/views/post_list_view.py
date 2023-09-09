from django.shortcuts import render, redirect
from django.http import HttpResponse
from dbpost.models.models import Post
from dbpost.forms.forms import *
# Create your views here.
def api_home_page(request, *args, **kwargs):
    return HttpResponse("<h1 style='text-align: center; margin-top: 30px;'>Welcome To Main Api Page.</h1>", content_type="text/html")

def post_list(request, *args, **kwargs):
    posts = Post.objects.all()
    response = {
        'posts': posts
    }
    return render(request, 'dbpost/post_lists.html', response)

def post_details_view(request, post_id, *args, **kwargs):
    post_details = Post.objects.filter(id=post_id).first()
    response = {
        'post': post_details,
    }
    return render(request, 'dbpost/post_details.html', response)

def post_create_form_view(request, *args, **kwargs):
    form = PostCreateForm()
    if request.method == 'POST':
        data = request.POST
        form = PostCreateForm(data=data)
        if form.is_valid():
            cl_data = form.cleaned_data
            post_obj = Post.objects.create(title=cl_data["title"], user_id=cl_data["user_id"])
            return redirect( 'dbpost:post_details_view', post_obj.id)
    return render(request, "dbpost/post_create.html", {'form': form})


