from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
# from rest_framework.settings import api_settings
# from rest_framework.permissions import IsAuthenticated

from profiles_api import serializers
from profiles_api import models
from profiles_api import permissions

class HelloApiView(APIView):
	"""Hello world API View"""
	serializer_class = serializers.HelloSerializer

	def get(self, request, format=None):
		"""Return a list of APIView features"""
		an_apiview = [
			'Uses HTTP methods as function (get, post, patch, put, delete)',
			'Is similar to a traditional Django View',
			'Give you the most control over you application logic',
			'is mapped manually to URLs'
		]
		return Response({'message':'Hello!','an_apiview':an_apiview})

	def post(self, request, format=None):
		"""Create a hello message with our name"""
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

	def put(self, request, format=None):
		"""Update an item"""
		return Response({'method': 'PUT'})

	def patch(self, request, format=None):
		"""Partially update an item"""
		return Response({'method': 'PATCH'})

	def delete(self, request, format=None):
		"""Delete an item"""
		return Response({'method': 'DELETE'})

class HelloViewSet(viewsets.ViewSet):
	"""Test API ViewSet"""
	serializer_class = serializers.HelloSerializer

	def list(self, request):
		"""Return a hello message."""

		a_viewset = [
            'Uses actions (list, create, retrieve, update, partial_update)',
            'Automatically maps to URLS using Routers',
            'Provides more functionality with less code',
        ]
		return Response({'message': 'Hello!', 'a_viewset': a_viewset})

	def create(self, request):
		"""create a new hello message"""
		serializer = self.serializer_class(data=request.data)

		if serializer.is_valid():
			name = serializer.validated_data.get('name')
			message = f'hello {name}'
			return Response({'message': message})
		else:
			return Response(
				serializer.errors,
				status=status.HTTP_400_BAD_REQUEST
			)

	def retrieve(self, request, pk=None):
		"""Handle getting an object by its ID"""
		return Response({'http_method': 'GET'})

	def update(self, request, pk=None):
		"""Handle updating an object"""
		return Response({'http_method': 'PUT'})

	def partial_update(self, request, pk=None):
		"""Handle updating part of an object"""
		return Response({'http_method': 'PATCH'})

	def destroy(self, request, pk=None):
		"""Handle removing an object"""
		return Response({'http_method': 'DELETE'})

class UserProfileViewSet(viewsets.ModelViewSet):
	"""Handle creating, creating and updating profiles"""
	serializer_class = serializers.UserProfileSerializer
	queryset = models.UserProfile.objects.all()
	authentication_classes = (TokenAuthentication,)
	permission_classes = (permissions.UpdateOwnProfile,)
	filter_backends = (filters.SearchFilter,)
	search_fields = ('name', 'email',)

class UserLoginApiView(ObtainAuthToken):
	"""Handle createing user authenticating tokens"""
	renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
