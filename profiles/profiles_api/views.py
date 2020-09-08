from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.filters import SearchFilter
from rest_framework import status
from profiles_api.serializers import HelloSerializer, UserProfileSerializer
from profiles_api.models import UserProfile
from profiles_api.permissions import UpdateOwnProfile

class HelloApiView(APIView):
    serializer_class = HelloSerializer

    def get(self, request, format=None):
        an_apiview=[
            'Uses HTTP methods as function (get, pos, putch, put, delete)',
            'Is similar to a traditionlal Django View',
            'GIves you the most control over your aplication logic',
            'Is mapped manually to URLs',
        ]

        return Response({'message': 'Hello World!', 'an_apiview': an_apiview})

    def post(self, request):
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
        return Response({'method': 'PUT'})
    
    def patch(self, request, pk=None):
        return Response({'method': 'PATCH'})
        
    def delete(self, request, pk=None):
        return Response({'method': 'DELETE'})


class HelloViewSet(ViewSet):
    serializer_class = HelloSerializer

    def list(self, request):
        a_viewset = [
            'Uses actions (list, create, retrieve, update, partial_update)',
            'Automatically maps to URLs using Routers',
            'Provides more functionality with less code',
        ]

        return Response({'message': 'Hello!', 'a_viewset': a_viewset})


    def create(self, request):
        serializer = self.serializer_class(data=request.data)
         
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        return Response({'http_method': 'DELETE'})


class UserProfileViewSet(ModelViewSet):
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (UpdateOwnProfile,)
    filter_backends = (SearchFilter,)
    search_fields = ('first_name', 'last_name', 'email', )