from pytube import YouTube
def download_video(url):
    try:
        yt = YouTube(url)
        video_stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
        video_stream.download()
        filename = video_stream.default_filename
        return filename
    except Exception as e:
        st.error(f"Error: {e}")
        return None