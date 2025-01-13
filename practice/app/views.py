from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView,ListCreateAPIView,RetrieveUpdateDestroyAPIView,GenericAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,UpdateModelMixin,DestroyModelMixin,RetrieveModelMixin
from rest_framework.viewsets import ReadOnlyModelViewSet,ModelViewSet

# 1. API view : A basic class for creating views , also you can create get,post,put,delete for request handling
class StudentApiView(APIView):
    def get(self,request):
        return Response({'status':'success','data':'get request'})
    def post(self,request):
        return Response({'status':'success','data':'post request'})
    def put(self,request,studentId):
        return Response({'status':'success','data':'put request','param':studentId})
    def delete(self,request,studentId):
        return Response({'status':'success','data':'delete request','param':studentId})
    
# 2. Generic Views : Pre-built views for common tasks like listing, creating, or retrieving objects.Saves you from writing repetitive code.Ex : ListAPIview,CreateAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView
class CourseListOrCreateGenericView(ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
class CourseRetrieveUpdateOrDeleteGenericView(RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

# 3. Mixins : Small building blocks to combine specific behaviors. Examples: CreateModelMixin, UpdateModelMixin, DestroyModelMixin.
class InstructorListOrCreateMixinView(CreateModelMixin,ListModelMixin,UpdateModelMixin,DestroyModelMixin,RetrieveModelMixin,GenericAPIView):
    queryset = Instructor.objects.all()
    serializer_class = InstructorSerializer
    
    def get(self,request,*args,**kwargs):
        if 'pk' in kwargs:
            return self.retrieve(request,*args,**kwargs)
        return self.list(request,*args,**kwargs)
    
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)
    
    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)
    
    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)
    
# 4. view set : Combines multiple actions (like list, retrieve, create) into one class. Works well with routers to generate URLs automatically. 
class DepartmentViewSetApi(ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer