from django.urls import path
from . import views

urlpatterns = [
    path("create-post",views.create_post,name="create-post"),
    path("find-posts",views.find_posts,name="find-posts"),
    path("find-post/<int:postId>",views.find_post,name="find-post"),
    path("update-post/<int:postId>",views.update_post,name="update-post"),
]