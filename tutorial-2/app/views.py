from django.shortcuts import render,HttpResponse
from .models import Post

from .serializers import PostSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response



@api_view(['POST'])
def create_post(request):
    if request.method == "POST":
        payload = request.data
        serializer = PostSerializer(data=payload)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
@api_view(['PUT','PATCH'])
def update_post(request,postId):
    post = Post.objects.get(id=postId)
    if Post.DoesNotExist:
        return Response({"error": "Post not found"})
    payload = request.data
    serializer = PostSerializer(post, data=request.data, partial=True)
    if serializer.is_valid():
        updated_post = serializer.save()
        return Response(PostSerializer(update_post).data)
    else:
        return Response(serializer.errors)

@api_view(['GET'])
def find_posts(request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def find_post(request,postId):
    post = Post.objects.get(id=postId)
    serializer = PostSerializer(post)
    return Response(serializer)