import yt_dlp

def download_video(url, resolution="720p"):
    try:
        print(f"Downloading video from: {url}")
        
        # yt-dlp 옵션 설정
        ydl_opts = {
            'format': 'bestvideo[height<=720]+bestaudio/best[height<=720]' if resolution == "720p" else 'best',  # 720p 또는 최고 화질
            'outtmpl': '%(title)s.%(ext)s'  # 파일 이름을 제목으로 설정
        }

        # 다운로드 실행
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=True)
            filename = ydl.prepare_filename(info_dict)
        
        return filename
    except Exception as e:
        # st.error(f"Error: {e}")
        return None

def download_audio(url):
    try:
        print(f"Downloading audio from: {url}")
        
        # yt-dlp 옵션 설정 (only audio)
        ydl_opts = {
            'format': 'bestaudio/best',  # 최고 음질
            'outtmpl': '%(title)s.%(ext)s',  # 파일 이름을 제목으로 설정
            'postprocessors': [{  # mp3로 변환 (원하면 주석 제거)
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }]
        }

        # 다운로드 실행
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=True)
            filename = ydl.prepare_filename(info_dict)
        
        return filename
    except Exception as e:
        # st.error(f"Error: {e}")
        return None
