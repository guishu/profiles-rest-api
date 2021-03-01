from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test API View"""

    def get(self, request, format=None):
        """Return a list of API view features"""
        an_apiview = [
            'Uses HTTP methodes as function (get, post, put, patch, delete)',
            'Is similar to a django view',
            'Gives ou the most control over your app logic',
            'Is mapped manyally to URLs',
        ]

        return Response({'message': 'Hello', 'an_apiview': an_apiview})
