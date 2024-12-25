from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test API View"""

    def get(self, request, format=None):
        """Retrun a list of APIView Features"""
        an_apiview = [
            'Uses HTTP methods as function (get,post,pach,put,delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control cover you application logic',
            'Is mapped manually to URLs',

        ]

        return Response({'message':'Hello!','an_apiview': an_apiview})
