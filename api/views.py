import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from django.conf import settings
from .serializers import GeoDataSerializer
from .models import GeoData


api_url = settings.EXTERNAL_API_URL
api_key = settings.EXTERNAL_API_KEY


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def store_view(request, ip):
    geo_data = requests.get(f'{api_url}{ip}?access_key={api_key}')
    serializer = GeoDataSerializer(data=geo_data.json())
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    else:
        return Response(serializer.errors, status=400)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def detail_view(request, ip):
    qs = GeoData.objects.filter(ip=ip)
    if qs.exists():
        serializer = GeoDataSerializer(qs.first())
        return Response(serializer.data, status=200)
    else:
        return Response({}, status=404)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_view(request):
    qs = GeoData.objects.all()
    serializer = GeoDataSerializer(qs, many=True)
    return Response(serializer.data, status=200)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def list_view(request, ip):
    qs = GeoData.objects.filter(ip=ip)
    if qs.exists():
        serializer = GeoDataSerializer(qs.first())
        serializer.delete()
        return Response(serializer.data, status=200)
    else:
        return Response({}, status=404)
