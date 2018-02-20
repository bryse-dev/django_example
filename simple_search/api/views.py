from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from simple_search.api.models import Search
from simple_search.api.serializers import SearchSerializer


@api_view(['GET', 'POST'])
def search(request, format=None):
    """
    List all previous searches or create a new one
    """
    if request.method == 'GET':
        searches = Search.objects.all()
        serializer = SearchSerializer(searches, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        data = JSONParser().parse(request)
        print(data)
        serializer = SearchSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400HTTP_400_BAD_REQUEST)
