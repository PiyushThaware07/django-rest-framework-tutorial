from django.urls import path,include
from . import views

urlpatterns = [
    path("",views.index,name="index"),
    path("api/v1/students/",views.studentListOrCreate,name="student-list-create"),
    path("api/v1/students/<int:studentId>",views.studentUpdateOrDelete,name="student-update-delete"),
    path("api/v1/courses/",views.CourseListOrCreateView.as_view(),name="course-list-create"),
    path("api/v1/courses/<int:courseId>",views.CourseUpdateOrDeleteView.as_view(),name="course-update-delete"),
]