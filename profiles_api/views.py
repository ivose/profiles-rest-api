from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated

#from profiles_api import serializers
#from profiles_api import models
#from profiles_api import permissions

class HelloApiView(APIView):
	"""Hello world API View"""

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
		"""Create a new item"""
		return Response({'new': 'item'})

	def put(self, request, format=None):
		"""Update an item"""
		return Response({'updated': 'item'})

	def patch(self, request, format=None):
		"""Partially update an item"""
		return Response({'partially_updated': 'item'})

	def delete(self, request, format=None):
		"""Delete an item"""
		return Response({'deleted': 'item'})
