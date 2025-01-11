from rest_framework import serializers
from .models import User,Post
from datetime import date



class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    # customer serializer to calculate age based on dob
    age = serializers.SerializerMethodField()  # sometime you dont want to create a column to database still you want to calculate value dyanmically and show to your json.
     # Get all the posts of the user
    posts = PostSerializer(many=True)
    # posts = PostSerializer(many=True,read_only=True) # if you just want to readonly not update user posts then add read_only to this.
    class Meta:
        model = User
        fields = "__all__"
        # exclude = ["created_at","updated_at"] either add manual fields else just excule fields.
        
    def get_age(self,obj):
        if obj.dob:
            today = date.today()
            age = today.year - obj.dob.year - ((today.month, today.day) < (obj.dob.month, obj.dob.day))
            return age
        return None
    
