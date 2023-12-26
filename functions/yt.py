from pytube import YouTube

def download_video(url, resolution="720p"):
    try:
        yt = YouTube(url)
        print(f"Downloading {yt.title}...")
        if resolution is "720p":
            video_stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
        if resolution is "max":
            video_stream = yt.streams.filter().order_by(
                'resolution').desc().first()

        if not video_stream:
            raise ValueError("No video stream found for the given URL.")

        video_stream.download()
        filename = video_stream.default_filename
        return filename
    except Exception as e:
        # st.error(f"Error: {e}")
        return None

def download_audio(url):
    try:
        yt = YouTube(url)
        print(f"Downloading {yt.title}...")
        audio_stream = yt.streams.filter(only_audio=True, file_extension='mp4').order_by('abr').desc().first()
        if not audio_stream:
            raise ValueError("No audio stream found for the given URL.")
        audio_stream.download()
        filename = audio_stream.default_filename
        return filename
    except Exception as e:
        # st.error(f"Error: {e}")
        return None

