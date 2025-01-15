from .models import *
from .serializers import *
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics,mixins
from rest_framework.viewsets import ModelViewSet


# Handle HTTP requests (GET, POST, PUT, DELETE, etc.).Allow greater customization for API behavior
class AuthorViews(APIView):
    def get(self,request):
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors,many=True)
        return Response({'status':'success','data':serializer.data})
    def post(self,request):
        payload = request.data
        serializer = AuthorSerializer(data=payload)
        if serializer.is_valid():
            serializer.save()
            return Response({'status':'success','data':serializer.data})
        return Response({'status': 'error', 'errors': serializer.errors})
    def put(self,request,authorId):
        author = Author.objects.get(id=authorId)
        payload = request.data
        serializer = AuthorSerializer(author, data=payload, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'status':'success','data':serializer.data})
        return Response({'status': 'error', 'errors': serializer.errors})
    def delete(self,request,authorId):
        author = Author.objects.get(id=authorId)
        author.delete()
        return Response({'status': 'success', 'message': f'Author {authorId} deleted'})


# Generic Views : Pre-built views for common patterns (e.g., displaying a list, showing a detail page, creating/updating/deleting objects).Reduces boilerplate code.
class BookListOrCreateViews(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
class BookRetrieveUpdateOrDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
# Viewset : Higher-level abstraction for APIs.Combine logic for list, retrieve, create, update, and delete operations in a single class.Often used with routers to automatically generate URL patterns.
class ReviewView(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    
# mixins : mixins provide reusable pieces of code that can be mixed into class-based views to implement common patterns such as create, retrieve, update, delete, and list actions.
class CategoryListOrCreateViews(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)
class CategoryRetrieveUpdateDestroyView(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    
    