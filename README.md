**Make sure FFmpeg is downloaded in your device.


If not,  download it from: https://www.ffmpeg.org, 
and add the folder path to your device's Environment variables.


When you specify formats like bestvideo+bestaudio in youtube-dl (or yt-dlp), it downloads the video and audio streams separately. This is common on platforms like YouTube, where video and audio are often stored as separate streams to allow for different resolutions and bitrates.

How it works:
Video Stream: The highest quality video stream is downloaded (usually without audio).
Audio Stream: The highest quality audio stream is downloaded separately.
Merging: FFmpeg is then used to merge the two streams into a single file.
