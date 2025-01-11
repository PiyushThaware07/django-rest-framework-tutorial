from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    content = serializers.CharField()
    status = serializers.CharField()
    likes = serializers.IntegerField()
    views = serializers.IntegerField()
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()
    is_active = serializers.BooleanField(read_only=True)
    
    def create(self,validated_data):
        return Post.objects.create(**validated_data)
    
    def update(self,instance,validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get('content', instance.content)
        instance.status = validated_data.get('status', instance.status)
        instance.likes = validated_data.get('likes', instance.likes)
        instance.views = validated_data.get('views', instance.views)
        instance.updated_at = validated_data.get('updated_at', instance.updated_at)
        instance.save()
        return instance
        