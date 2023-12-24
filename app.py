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
        # st.write("Written by TJ.Kim ☕")
        st.markdown("---")

    # User input for YouTube URL
    url = st.text_input(label="Enter URL:")
    # st.write("Entered URL:", url)

    if st.button("video:max 720p)"):
        filename=None
        for _ in range(10):
            try:
                filename = download_video(url)
                break
            except:
                pass


        if filename is not None:
            st.success(f"Video downloaded successfully: {filename}")
            # Display download button
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
            st.error("Failed to download video.")

    if st.button("audio"):
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
            st.error("Failed to download audio.")
if __name__ == "__main__":
    main()
