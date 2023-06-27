# local-video-portal

Local video portal written in django for tutorial videos. Written in django.

## How to run for production

```bash
git clone https://github.com/Jean28518/local-video-portal.git
cd local-video-portal
docker-compose up -d
```

### How to update (for new version or videocontent)

```bash
git pull
docker-compose up -d --build
```

You can reach the server under the port 21000.

## How to run for development

```bash
cd videoportal
python3 manage.py runserver
```

## How to create video directory

You need to place the new content in `videoportal/static/videoportal/`.
A demo entry is available.
After changing content a `docker-compose up -d --build` is required.

### Structure

- Year (2023)
  - Month (06)
    - Video_Title (This_is_a_cool_video_title)
      - description.html
      - video.mp4
      - thumbnail.jpg
