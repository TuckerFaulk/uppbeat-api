from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Tracks
from .serializers import TracksSerializer


class TracksList(generics.ListCreateAPIView):
    queryset = Tracks.objects.all()
    serializer_class = TracksSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = [
        'track_name',
        'artist',
        'album',
    ]
    filterset_fields = ['category']


class TracksDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tracks.objects.all()
    serializer_class = TracksSerializer
