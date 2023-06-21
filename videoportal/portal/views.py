from django.shortcuts import render
from django.http import HttpResponse
import portal.video_finder




# Create your views here.
def index(request):
    video_entries = portal.video_finder.get_all_videos()
    search = request.GET.get('q', '')
    print(video_entries)
    return render(request, "portal/video_overview.html", {"video_entries": video_entries , "search": search})

def video(request, video_id):
    video_entries = portal.video_finder.get_all_videos()
    video_entry = video_entries[video_id]
    print(video_entry)
    return render(request, "portal/video_singleview.html", {"video_entry": video_entry})
