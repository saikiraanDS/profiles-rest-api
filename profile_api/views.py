from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


from profile_api import serializers


class HelloApiView(APIView):
    """Test API View"""
    serializers_class = serializers.HelloSerializer
    def get(self, request, format=None):
        """Retrun a list of APIView Features"""
        an_apiview = [
            'Uses HTTP methods as function (get,post,pach,put,delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control cover you application logic',
            'Is mapped manually to URLs',

        ]

        return Response({'message':'Hello!','an_apiview': an_apiview})

    def post(self, request):
        """Create a hello message with our name"""
        serializer = self.serializers_class(data=request.data)


        if serializer.is_valied():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
             )

    def put(self,request,pk=None):
        """Handle updating an object"""
        return Response({'method':'PUT'})

    def patch(self, request, pk=None):
        """Handle a partial update of an object"""
        return Response({'method':'PATCH'})

    def delete(self,request, pk=None):
        """delete an object"""
        return Response({'method':'DELETE'})
