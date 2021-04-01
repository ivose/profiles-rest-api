from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# from rest_framework.settings import api_settings
# from rest_framework.permissions import IsAuthenticated

from profiles_api import serializers
# from profiles_api import models
# from profiles_api import permissions

class HelloApiView(APIView):
	"""Hello world API View"""
	serializers_class = serializers.HelloSerializer

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
		serializer = self.serializers_class(data=request.data)

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
