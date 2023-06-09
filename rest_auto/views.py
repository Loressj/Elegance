from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from core.models import Auto
from .serializers import AutoSerializer

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.

@csrf_exempt
@api_view(['GET','POST'])
@permission_classes((IsAuthenticated,))

def lista_autos(request):

# Listado Bicicleta
    if request.method == 'GET':
        Auto = Auto.objects.all()
        serializer = AutoSerializer(auto, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = AutoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        


@api_view(['GET','PUT', 'DELETE'])
@permission_classes((IsAuthenticated,))

def detalle_autos(request, id):
    try:
        auto = Auto.objects.get(id=id)
    except Auto.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AutoSerializer(Auto)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = AutoSerializer(Auto, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        Auto.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)