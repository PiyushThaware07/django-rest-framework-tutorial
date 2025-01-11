from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework import generics,mixins
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import DjangoModelPermissions



# * --------------( viewsets )-------------------------------------------------
class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class  = BookSerializer
    
    
# * ---------------( generic views )-------------------------------------------
class AuthorListCreateView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class AuthorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    
# List all books written by a specific author
class BooksByAuthorView(generics.ListAPIView):
    serializer_class = BookSerializer
    def get_queryset(self):
        pk = self.kwargs['pk']
        return Book.objects.filter(author=pk)

# Create a new book for a specific author
class CreateBookByAuthorView(generics.CreateAPIView):
    serializer_class = BookSerializer
    def perform_create(self, serializer):
        pk = self.kwargs['pk']
        author = Author.objects.get(pk=pk)
        serializer.save(author=author)    

# * -------------( Api views )-------------------------------------------------
class TagApiView(APIView):
    def get(self, request):
        tags = Tag.objects.all()
        serializer = TagSerializer(tags, many=True)
        return Response(serializer.data)
    
    def post(self,request):
        payload = request.data
        serializer = TagSerializer(data=payload)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

# * --------------( mixins with generic )---------------------------------------------------
class ReviewListView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ReviewDetailView(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [DjangoModelPermissions]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)