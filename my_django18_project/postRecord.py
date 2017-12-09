from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from profiles.records import Record

@api_view(['GET', 'POST'])
def create(req):

    if req.method == 'GET':
        #return Response(data)
        return Response(status=status.HTTP_201_CREATED)
    elif req.method == 'POST':
        return Response(status=status.HTTP_201_CREATED)
        #return Response(serializer.data, status=status.HTTP_201_CREATED)
        #return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)