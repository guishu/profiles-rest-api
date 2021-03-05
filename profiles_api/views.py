from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from profiles_api import serializers
from profiles_api import models
from profiles_api import permissions


class HelloApiView(APIView):
    """Test API View"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Return a list of API view features"""
        an_apiview = [
            'Uses HTTP methodes as function (get, post, put, patch, delete)',
            'Is similar to a django view',
            'Gives ou the most control over your app logic',
            'Is mapped manyally to URLs',
        ]

        return Response({'message': 'Hello', 'an_apiview': an_apiview})

    def post(self, request):
        """Create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        """Handle updating an object"""
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """Handle partial updating an object"""
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """Handle partial updating an object"""
        return Response({'method': 'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    """Test API viewser"""
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Return an hello message"""
        a_viewset = [
            'Uses actions (list, create, retreive, update, partial update)',
            'Automatically maps to urls using routers',
            'Provides more functionalities with less code'
        ]

        return Response({
            'message': 'Hello',
            'a_viewset': a_viewset
        })

    def create(self, request):
        """Create a new hello message"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retreive(self, request, pk=None):
        """handle getting an object by id"""
        return Response({'method': 'GET'})

    def update(self, request, pk=None):
        """handle getting an object by id"""
        return Response({'method': 'PUT'})

    def partial_update(self, request, pk=None):
        """handle getting an object by id"""
        return Response({'method': 'PATCH'})

    def destroy(self, request, pk=None):
        """handle getting an object by id"""
        return Response({'method': 'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email')


class UserLoginApiView(ObtainAuthToken):
    """Handle creating user authenticatoin tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
