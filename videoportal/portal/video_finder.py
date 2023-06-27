import os
from django.conf import settings

# Video Structure
# - Year (2023)
#   - Month (06)
#     - Video_Title (This_is_a_cool_video_title)
#       - description.html
#       - video.mp4
#       - thumbnail.jpg
def get_all_videos():
    # Get Setting STATICFILES_DIRS
    
    content_dir = os.path.join(settings.STATICFILES_DIRS[0], "videoportal", "content")
    videos = []
    id = 0
    for year in os.listdir(content_dir):
        for month in os.listdir(os.path.join(content_dir, year)):
            for video in os.listdir(os.path.join(content_dir, year, month)):
                video_entry = {"description" : "", "thumbnail" : "", "video" : "", "title" : video.replace("_", " ")}
                for file in os.listdir(os.path.join(content_dir, year, month, video)):
                    if file.endswith(".html"):
                        # Read the description file
                        with open(os.path.join(content_dir, year, month, video, file), "r") as f:
                            video_entry["description"] = f.read()
                    elif file.endswith(".jpg"):
                        video_entry["thumbnail"] = os.path.join("static", "videoportal", "content", year, month, video, file)
                    elif file.endswith(".mp4"):
                        video_entry["video"] = os.path.join("static", "videoportal", "content", year, month, video, file)
                video_entry["id"] = id
                id += 1

                # Generate description preview
                video_entry["description_preview"] = video_entry["description"][:250] + "..."                

                videos.append(video_entry)
    return videos