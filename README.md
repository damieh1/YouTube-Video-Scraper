# YouTube Playlist Downloader with YouTube API and `yt-dlp`

Download all videos from a YouTube playlist, including YT shorts, using the YouTube API via Python. Retrieved videos include metadata and videos in the best quality available.

## Features

- Retrieves video titles and IDs from a specified YouTube playlist using the YouTube Data API.
- Downloads videos using `yt-dlp` in the best available quality (video and audio combined).
- Stores downloaded videos in a specified folder.
- Outputs video metadata in a pandas DataFrame.

## Requirements

Make sure you have the following installed:

- Python 3.6 or higher
- `yt-dlp`
- `google-api-python-client`
- `pandas`
- `os`
- `pytube`

## Installation

1. **Clone the repository:**

```bash
git clone https://github.com/damieh1/YouTube-Video-Scraper.git
cd YouTube-Video-Scraper
