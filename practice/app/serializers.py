from .models import *
from rest_framework import serializers
from rest_framework.validators import ValidationError



class InstructorSerializer(serializers.ModelSerializer):
    courses = serializers.PrimaryKeyRelatedField(queryset=Course.objects.all(), many=True,)
    class Meta:
        model = Instructor
        fields = "__all__"
        
class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = "__all__"
        
class CourseSerializer(serializers.ModelSerializer):
    is_duration_long = serializers.SerializerMethodField()
    # Use a nested serializer for the related Instructor
    instructor = InstructorSerializer()
    class Meta:
        model = Course
        fields = "__all__"
    def validate(self,data):
        if data['duration'] > 5:
            raise ValidationError("duration can not be more that 5")
        return data
    def get_is_duration_long(self,obj):
        return obj.duration > 3

