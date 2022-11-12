from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


from .serializers import RegisterSerializer,MyTokenObtainPairSerializer
from . models import User
from rest_framework import generics


class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

class Users(generics.ListAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

class UsersDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer
    # lookup_field = "pk"

class UserProfile(generics.RetrieveAPIView):
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = RegisterSerializer

    def get_object(self):
        obj = get_object_or_404(User, pk=self.request.user.id)
        return obj


    # def get(self, request):
    #     content = User.objects.filter(pk=request.user.id)
    #     serializer = UpdateSerializer(content)
    #     return Response(serializer.data)
    # queryset = User.objects.all()
    # permission_classes = (IsAuthenticated,)
    # serializer_class = RegisterSerializer