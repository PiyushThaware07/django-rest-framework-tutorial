from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r"books",views.BookViewSet)


urlpatterns = [
    path("api/v1/",include(router.urls)),
    # generic views
    path('api/v1/authors/', views.AuthorListCreateView.as_view(), name='author-list-create'),
    path('api/v1/authors/<int:pk>/', views.AuthorRetrieveUpdateDestroyView.as_view(), name='author-retrieve-update-destroy'),
    # api view
    path('api/v1/tags/', views.TagApiView.as_view(), name='tag-api-view'),
    # mixin view with geneic views
    path('api/v1/reviews/', views.ReviewListView.as_view(), name='review-list'),
    path('api/v1/reviews/<int:pk>/', views.ReviewDetailView.as_view(), name='review-detail'),
    
    # dynamic routes
    path("api/v1/authors/<int:pk>/books/", views.BooksByAuthorView.as_view(), name="author-books"),
    path('api/v1/authors/<int:pk>/books/create/', views.CreateBookByAuthorView.as_view(), name='create-book-by-author'),
]