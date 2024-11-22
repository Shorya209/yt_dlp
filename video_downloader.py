import yt_dlp #YouTube Download Python
import time
import os
import sys

url = sys.argv[1]
if url in ('-h', '-help'):
    print('Syntax: "{yt url}" "{folder path}" "{file name}"')
    sys.exit(0)
path = sys.argv[2]
fileName = sys.argv[3]

print('\n')

ydl_opts = {
    'format': 'bestvideo+bestaudio/best',
    'outtmpl': os.path.join(path, fileName), #output template
    'noplaylist': True,
    'postprocessors': [{  # Post-processing options
        'key': 'FFmpegVideoConvertor',  # Use FFmpeg for conversion
        'preferedformat': 'mp4',  # Convert to MP4
    }],
    # 'writesubtitles': True,
    # 'subtitleslangs': ['en']
}

start_time = time.time()

try:
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            info = ydl.extract_info(url, download=False) #Extract Video info if available
            print(f'\nTitle: {info.get('title')}\nViews: {info.get('view_count'):,}\nLikes: {info.get('like_count'):,}\nYTChannel: {info.get('uploader')}\nDuration: {info.get('duration')}\n')
        except Exception as e:
            print('\nInfo Cannot be extracted!')
        ydl.download([url])
        print("\nDownload completed!")
except Exception as e:
    print('\nDownload Failed!')

end_time = time.time()
print(f'Runtime: {float(end_time-start_time):.2f} seconds')