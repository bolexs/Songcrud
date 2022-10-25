from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import SongSerializer, UpdateSongSerializer
from django.shortcuts import get_object_or_404
# Create your views here.

class SongViewSet(viewsets.ModelViewSet):
    serializer_class = SongSerializer

    def get_queryset(self):
        return Song.objects.all()
   
