from . import views
from django.urls import path,include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"reviews",views.ReviewView,basename="reviews")

urlpatterns = [
    path("api/v1/authors/",views.AuthorViews.as_view(),name="authors"),
    path("api/v1/authors/<int:authorId>/",views.AuthorViews.as_view(),name="authors-by-id"),
    path("api/v1/books/",views.BookListOrCreateViews.as_view(),name="book-list-create"),
    path("api/v1/books/<int:pk>/",views.BookRetrieveUpdateOrDelete.as_view(),name="book-retrieve-update-delete"),
    path("api/v1/",include(router.urls)),
    path("api/v1/categories/",views.CategoryListOrCreateViews.as_view(),name="category-list-create"),
    path("api/v1/categories/<int:pk>",views.CategoryRetrieveUpdateDestroyView.as_view(),name="category-retrieve-update-delete"),
]