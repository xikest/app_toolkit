import os
import streamlit as st
from functions.yt import download_video, download_audio
import base64



def main():
    # Basic setting
    st.set_page_config(
        page_title="Downloader",
        layout="wide",
        initial_sidebar_state="collapsed"
    )

    # Title
    st.header("Downloader")

    # Sidebar
    with st.sidebar:
        # Basic description
        # st.subheader("YouTube Downloader")
        st.write("Private project")
        st.markdown("---")
        st.write("Written by TJ.Kim ☕")
        st.markdown("---")

    # User input for YouTube URL
    url = st.text_input(label="Enter URL:")
    # st.write("Entered URL:", url)
    col1, col2 = st.columns(2)
    with col1:
        resolution = st.radio("Select resolution:", ["720p", "max"])
        if st.button("video"):
            filename=None
            for _ in range(10):
                try:
                    filename = download_video(url, resolution)
                    break
                except:
                    pass


            if filename is not None:
                st.success(f"Video downloaded successfully: {filename}")
                # Display download button.
                file_path = os.path.join(os.getcwd(), f"{filename}")
                with open(file_path, "rb") as file:
                    video_file = file.read()
                    st.download_button(
                        label="Download Video",
                        data=video_file,
                        file_name=f"{filename}",
                        mime="video/mp4"
                    )
            else:
                st.error("Failed to download video.", icon= "🚨")
    with col2:
        if st.button("audio, mp4"):
            filename = None
            for _ in range(10):
                try:
                    filename = download_audio(url)
                    break
                except:
                    pass

            if filename is not None:
                st.success(f"Audio downloaded successfully: {filename}")
                # Display download button
                file_path = os.path.join(os.getcwd(), f"{filename}")
                with open(file_path, "rb") as file:
                    video_file = file.read()
                    st.download_button(
                        label="Download Audio",
                        data=video_file,
                        file_name=f"{filename}",
                        mime="audio/mp4"
                    )
            else:
                st.error("Failed to download audio.", icon= "🚨")
if __name__ == "__main__":
    main()
