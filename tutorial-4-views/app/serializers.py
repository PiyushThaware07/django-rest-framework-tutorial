from .models import *
from rest_framework import serializers


class AuthorSerializer(serializers.ModelSerializer):
    book_count = serializers.SerializerMethodField()
    class Meta:
        model = Author
        fields = "__all__"
    def get_book_count(self,obj):
        return obj.book_set.count()


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"



class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Review
        fields = "__all__"

    
    
        
class BookSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)
    class Meta:
        model = Book
        fields = "__all__"
    