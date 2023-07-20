from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("video/<int:video_id>", views.video, name="video"),
    path("videopath/", views.videopath, name="videopath"),
]