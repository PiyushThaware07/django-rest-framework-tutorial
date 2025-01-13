from .models import *
from .serializers import *
from rest_framework.decorators import api_view,APIView
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated

@api_view(["GET"])
def index(request):
    return Response({"status":"success","message":"Server Running"})



@api_view(["GET","POST"])
def studentListOrCreate(request):
    if request.method == "POST":
        payload = request.data
        serializer = StudentSerializer(data=payload)
        if serializer.is_valid():
            serializer.save()
            return Response({"status":"success","data":serializer.data})
        return Response({'status':'failed','error':serializer.errors})
    else:
        students = Student.objects.all()
        serializer = StudentSerializer(students,many=True)
        return Response({"status":"success","data":serializer.data})



@api_view(["GET","PUT","DELETE"])
def studentUpdateOrDelete(request,studentId):
    try:
        student = Student.objects.get(id=studentId)
    except Student.DoesNotExist:
        return Response({"status": "error", "message": "Student not found"})
    if request.method == "GET":
        serializer = StudentSerializer(student)
        return Response({"status": "success", "data": serializer.data})
    elif request.method == "PUT":
        serializer = StudentSerializer(student,request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status':'success','data':'update successfully!'})
        return Response({'status':'failed','data':serializer.errors})
    elif request.method == "PATCH":
        serializer = StudentSerializer(student, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'status':'success','data':'update successfully!'})
        return Response({'status':'failed','data':serializer.errors})
    elif request.method == "DELETE":
        student.delete()
        return Response({'status':'success','data':'deleted successfully!'})
        
    
        
# Course List or Create View
class CourseListOrCreateView(APIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return Response({'status': 'success', 'data': serializer.data})

    def post(self, request):
        payload = request.data
        serializer = CourseSerializer(data=payload)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', 'data': serializer.data})
        return Response({'status': 'failed', 'error': serializer.errors})


# Course Update or Delete View
class CourseUpdateOrDeleteView(APIView):
    def get_object(self, courseId):
        try:
            return Course.objects.get(id=courseId)
        except Course.DoesNotExist:
            return None

    def get(self, request, courseId):
        course = self.get_object(courseId)
        if course is None:
            return Response({"status": "error", "message": "Course not found"})

        serializer = CourseSerializer(course)
        return Response({"status": "success", "data": serializer.data})

    def put(self, request, courseId):
        course = self.get_object(courseId)
        if course is None:
            return Response({"status": "error", "message": "Course not found"})

        serializer = CourseSerializer(course, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', 'data': 'updated successfully!'})
        return Response({'status': 'failed', 'data': serializer.errors})

    def patch(self, request, courseId):
        course = self.get_object(courseId)
        if course is None:
            return Response({"status": "error", "message": "Course not found"})

        serializer = CourseSerializer(course, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', 'data': 'updated successfully!'})
        return Response({'status': 'failed', 'data': serializer.errors})

    def delete(self, request, courseId):
        course = self.get_object(courseId)
        if course is None:
            return Response({"status": "error", "message": "Course not found"})

        course.delete()
        return Response({'status': 'success', 'data': 'deleted successfully!'})