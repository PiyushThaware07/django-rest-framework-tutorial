from rest_framework import serializers
from .models import *


class CourseSerializer(serializers.ModelSerializer):
    # Nested serializer to list all students enrolled in the course
    students = serializers.StringRelatedField(many=True)
    class Meta:
        model = Course
        fields = "__all__"
        
        
class StudentSerializer(serializers.ModelSerializer):
    # Nested serializer to list all courses the student is enrolled in
    courses = CourseSerializer(many=True,read_only=True)
    class Meta:
        model = Student
        fields = "__all__"
    
    # * Field-level validation for age
    def validate_age(self,value):
        if value < 18:
            raise serializers.ValidationError("Age must be at least 18.")
        return value
    
    # * Object-level validation
    def validate(self,data):
        if not data['email'].endswith("@gmail.com"):
            raise serializers.ValidationError("Email must belong to the @gmail.com")
        return data
    

    