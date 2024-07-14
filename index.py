import streamlit as st
from PIL import Image
import pytesseract
import pdf2image
from pdf2image import convert_from_path, convert_from_bytes
from pdf2image.exceptions import (
    PDFInfoNotInstalledError,
    PDFPageCountError,
    PDFSyntaxError,
)
from process.easy_ocr import process as easy_ocr_process
from process.tesseract_ocr import process as tesseract_ocr_process

st.title("Parse Vision")
st.write("Visualise what OCR libraries see in your documents")

uploaded_file = st.file_uploader("Upload a file", type=["pdf"])

if uploaded_file is not None:
    images = convert_from_bytes(uploaded_file.getvalue())
    with st.spinner("Processing... this may take several seconds"):
        processed_images = easy_ocr_process(images)
        processed_images2 = tesseract_ocr_process(images)
        # create 2 tabs for each OCR library
        # tab 1 = easy_ocr
        # tab 2 = pytesseract
        tab1, tab2 = st.tabs(["EasyOCR", "Tesseract"])
        with tab1:
            for i, image in enumerate(processed_images):
                st.image(image, caption=f"Page {i}", use_column_width=True)
        with tab2:
            for i, image in enumerate(processed_images2):
                st.image(image, caption=f"Page {i}", use_column_width=True)
