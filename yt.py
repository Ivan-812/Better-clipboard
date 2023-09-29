import json
import yt_dlp


def get_video_info(urls, ydl_opts={}):
    for url in urls:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            # ℹ️ ydl.sanitize_info makes the info json-serializable
            print(json.dumps(ydl.sanitize_info(info)))

def download(urls, ydl_opts={}):
    # ℹ️ See help(yt_dlp.YoutubeDL) for a list of available options and public functions
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download(urls)


def video(urls, opts={}):
    format = 'bestvideo[height<=360]+bestaudio/best'
    # format = 'bestvideo+bestaudio'
    preferedformat = 'mp4' # one of avi, flv, mkv, mp4, ogg, webm
    video_opts = {
        'format': format,
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': preferedformat,
        }]
    }
    opts.update(video_opts)
    download(urls, opts)

def audio(urls, opts={}):
    audio_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3'
        }],
    }
    opts.update(audio_opts)
    download(urls, opts)


if __name__ == '__main__':
    URLS = []
    URLS.append('https://youtu.be/gPL0P8nHBM0')
    # URLS.append('https://www.youtube.com/watch?v=OPno2a93-5Y')

    dl_opts = {'outtmpl': 'C:/Users/02005048/Videos/yt-download/%(title)s-%(id)s.%(ext)s'}

    opts = {}
    opts.update(dl_opts)

    # get_video_info(URLS)
    # download(URLS, opts)
    video(URLS, opts)


