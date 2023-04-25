from django.urls import path
from tracks import views

urlpatterns = [
    path('tracks/', views.TracksList.as_view()),
    path('tracks/<int:pk>/', views.TracksDetail.as_view()),
]
