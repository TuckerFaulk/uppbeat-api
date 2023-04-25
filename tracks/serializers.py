from rest_framework import serializers
from .models import Tracks


class TracksSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tracks()
        fields = [
            'id', 'track_name', 'artist', 'album', 'image',
            'premium_track', 'category', 'add_playlist', 'add_favourite',
        ]
