from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
from .models import *

# Create your views here.
def create_post(request):
    return HttpResponse("create_post")

def find_all_posts(request):
    posts = Post.objects.all()
    data = {"posts":list(posts.values())}
    return JsonResponse(data)

def find_post_By_id(request,postId):
    print(postId)
    return HttpResponse("hello")