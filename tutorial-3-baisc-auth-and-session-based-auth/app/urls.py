from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet,PostListView,PostDetailView

router = DefaultRouter()
router.register(r"users",UserViewSet)

urlpatterns = [
    path('api/',include(router.urls)),
     path('api/posts/', PostListView.as_view(), name='post-list'), 
    path('api/posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
]