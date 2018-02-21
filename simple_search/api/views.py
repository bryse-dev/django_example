from rest_framework import status
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from simple_search.api.models import Search
from simple_search.api.serializers import SearchSerializer
from rest_framework.views import APIView


class SearchView(APIView):
    def get(self, request):
        """
        List all previous searches
        """
        searches = Search.objects.all()
        serializer = SearchSerializer(searches, many=True)
        return Response(serializer.data)

    def post(self, request):
        """
        Create a new search
        """
        data = JSONParser().parse(request)
        serializer = SearchSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400HTTP_400_BAD_REQUEST)

    def put(self, request):
        """
        Initiate an existing search
        """
        data = JSONParser().parse(request)
        if "id" in data:
            search = Search.objects.get(id=data["id"])
            if search:
                search.status = 'RUNNING'
                search.save()
                return Response("Search started", status=status.HTTP_200_OK)
            return Response("Could not find search with the supplied ID", status=status.HTTP_404_NOT_FOUND)
        return Response("Please provide a proper JSON request with an 'id' field", status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        """
        Remove an existing search
        """
        data = JSONParser().parse(request)
        if "id" in data:
            search = Search.objects.get(id=data["id"])
            if search:
                search.delete()
                return Response("Search removed", status=status.HTTP_200_OK)
            return Response("Could not find search with the supplied ID", status=status.HTTP_404_NOT_FOUND)
        return Response("Please provide a proper JSON request with an 'id' field", status=status.HTTP_400_BAD_REQUEST)
