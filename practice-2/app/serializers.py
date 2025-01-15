from .models import *
from rest_framework import serializers
from rest_framework.validators import ValidationError
        
class BookSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    class Meta:
        model = Book
        fields = "__all__"
    def validate(self,obj):
        if obj['name'] == "Piyush Thaware":
            raise ValidationError(detail="name can not be empty!")
        return obj
        
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True,read_only=True)
    books_count = serializers.SerializerMethodField()
    class Meta:
        model = Author
        fields = "__all__"
    def get_books_count(self, obj):
        return obj.books.count()  
        
        

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"
        
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"