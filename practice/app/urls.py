from . import views
from django.urls import path,include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"departments",views.DepartmentViewSetApi,basename="departments"),

urlpatterns = [
    path("api/v1/students/",views.StudentApiView.as_view(),name="students"),
    path("api/v1/students/<int:studentId>",views.StudentApiView.as_view(),name="students"),
    path("api/v1/courses/",views.CourseListOrCreateGenericView.as_view(),name="courses-list-create"),
    path("api/v1/courses/<int:pk>",views.CourseRetrieveUpdateOrDeleteGenericView.as_view(),name="courses-retrieve-update-delete"),
    path("api/v1/instructors/",views.InstructorListOrCreateMixinView.as_view(),name="instructors-list-create"),
    path("api/v1/instructors/<int:pk>",views.InstructorListOrCreateMixinView.as_view(),name="instructors-retrieve-update-delete"),
    path("api/v1/",include(router.urls)),
]