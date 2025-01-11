from django.urls import path
from . import views

urlpatterns = [
    path("create-post",views.create_post,name="create_post"),
    path("find-all-post",views.find_all_posts,name="find_all_post"),
    path("find-post-by-id/<int:postId>",views.find_post_By_id,name="find_post_by_id"),
]