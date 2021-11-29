from django.shortcuts import render
from rest_framework import views, authentication, permissions, status
from rest_framework.response import Response
from django.contrib.auth.models import User
from ..models import Proveedor, Cliente
from ..serializers import UserSerializer, UserClienteSerializer, UserProveedorSerializer, UserCreationSerializer

class UserRetrieve(views.APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user) 
        return Response(data=serializer.data, status=status.HTTP_200_OK)




class UserClienteCreate(views.APIView):
    def post(self, request):
        serializer = UserCreationSerializer(data=request.data)
        if serializer.is_valid():
            user = User.objects.create_user(username=serializer.validated_data['username'], password=serializer.validated_data['password'])
            Cliente.objects.create(user=user, nombre=request.data['nombre'], direccion=request.data['direccion'])
            return Response(status=status.HTTP_201_CREATED)


class UserProveedorCreate(views.APIView):
    def post(self, request):
        serializer = UserCreationSerializer(data=request.data)
        if serializer.is_valid():
            user = User.objects.create_user(username=serializer.validated_data['username'], password=serializer.validated_data['password'])
            Proveedor.objects.create(user=user, nombre=request.data['nombre'], direccion=request.data['direccion'], nit=request.data['nit'])
            return Response(status=status.HTTP_201_CREATED)