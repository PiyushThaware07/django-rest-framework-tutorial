from .models import *
from .serializers import *
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.authtoken.models import Token


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]
    
class RegistrationView(APIView):
    def post(self,request,*args,**kwargs):
        payload = request.data
        serializer = RegistrationSerializer(data=payload)
        if serializer.is_valid():
            serializer.save()
            return Response({
               'message': 'User registered successfully!',
               'user' : serializer.data
            })
        else:
            return Response(serializer.errors)

class LogoutView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self, request, *args, **kwargs):
        try:
            token = Token.objects.get(user=request.user)
            token.delete()
            return Response({"message": "User logged out successfully!"})
        except Token.DoesNotExist:
             return Response({"error": "Token not found"})
    