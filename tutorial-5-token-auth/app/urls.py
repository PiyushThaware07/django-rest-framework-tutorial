from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register(r"products",views.ProductViewSet)

urlpatterns = [
    path("api/v1/",include(router.urls)),
    path("api/v1/auth/signin",obtain_auth_token,name="signin"),
    path("api/v1/auth/signup",views.RegistrationView.as_view(),name="signup"),
    path("api/v1/auth/signout",views.LogoutView.as_view(),name="signout"),
]