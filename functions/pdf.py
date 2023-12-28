import fitz  # PyMuPDF
import requests
from io import BytesIO
import streamlit as st


def pdf_to_text(data, is_url=True):
    if is_url:
        response = requests.get(data)
        pdf_bytes = BytesIO(response.content)
    else:
        pdf_bytes = BytesIO(data.read())

    text = ""
    try:
        with fitz.open("pdf", pdf_bytes) as pdf_document:
            for page_number in range(pdf_document.page_count):
                page = pdf_document[page_number]
                page_text = page.get_text().lower().strip()
                text += page_text
    except Exception as e:
        st.error(f"Error: {e}")

    return text