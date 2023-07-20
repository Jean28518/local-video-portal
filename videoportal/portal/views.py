from django.shortcuts import render, redirect
from django.http import HttpResponse
import portal.video_finder


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


def videopath(request):
    video_entries = portal.video_finder.get_all_videos()
    path = request.GET.get("path", "-1/-1/-1!")

    # Get video id by searching for the path in the video paths
    video_id = -1
    for video_entry in video_entries:
        if path in video_entry["video"]:
            video_id = video_entry["id"]
            break

    if video_id == -1:
        return HttpResponse("Video not found!", status=404)
    
    # Redirect to video site
    return redirect("video", video_id=video_id)
