from django.shortcuts import render
from django.http import HttpResponse
import portal.video_finder




# Create your views here.
def index(request):
    video_entries = portal.video_finder.get_all_videos()
    print(video_entries)
    return render(request, "portal/video_view.html", {"video_entries": video_entries})