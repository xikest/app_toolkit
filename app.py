import os
import streamlit as st
from functions.yt import *
from functions.pdf import *



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


    tab1, tab2 = st.tabs(["YT", "PDF"])
    with tab1:
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
                        audio_file = file.read()
                        st.download_button(
                            label="Download Audio",
                            data=audio_file,
                            file_name=f"{filename}",
                            mime="audio/mp3"
                        )
                else:
                    st.error("Failed to download audio.", icon= "🚨")


    with tab2:
        st.title("PDF Text Extractor")

        data_source = st.radio("Select data source:", options=['URL', 'Upload PDF File'])

        with st.form(key='pdf_form'):
            if data_source == 'URL':
                data_input = st.text_input("Enter PDF URL:", key="pdf_input")
            else:
                data_input = st.file_uploader("Upload PDF file", type=["pdf"], key="pdf_input")

            submitted = st.form_submit_button(label='Submit')

        if submitted:
            if data_source == 'URL':
                text = pdf_to_text(data_input, is_url=True)
            else:
                text = pdf_to_text(data_input, is_url=False)

            st.subheader("Extracted Text:")

            # Display extracted text
            st.text_area("Text", value=text, height=400)

            # Download button
            download_button = st.download_button(
                label="Download Text",
                data=text.encode('utf-8'),
                file_name="extracted_text.txt",
                key="download_button"
            )

if __name__ == "__main__":
    main()
