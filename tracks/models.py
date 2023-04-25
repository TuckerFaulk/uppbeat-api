from django.db import models


class Tracks(models.Model):

    category_filter_choices = [
        ("Jazz", "Jazz"),
        ("Rock", "Rock"),
        ("Chill", "Chill"),
    ]

    track_name = models.CharField(max_length=100, blank=False)
    artist = models.CharField(max_length=100, blank=False)
    album = models.CharField(max_length=100, blank=False)
    image = models.ImageField(
        upload_to='images/', default='../uppbeat_logo_gh4ogf'
    )
    premium_track = models.BooleanField(default=False)
    category = models.CharField(
        max_length=32, choices=category_filter_choices, default='Jazz'
    )
    add_playlist = models.BooleanField(default=False)
    add_favourite = models.BooleanField(default=False)

    class Meta:
        ordering = ['track_name']

    def __str__(self):
        return f"{self.track_name} - {self.artist}"
