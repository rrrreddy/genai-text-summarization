import logging
import pdfplumber
import docx
from utils.logging_utils import setup_logging

setup_logging()

def read_text_file(file_path):
    logging.info(f"Reading text file: {file_path}")
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except Exception as e:
        logging.error(f"Failed to read text file: {e}")
        return None

def read_pdf_file(file_path):
    logging.info(f"Reading PDF file: {file_path}")
    text = ''
    try:
        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text
        return text
    except Exception as e:
        logging.error(f"Failed to read PDF file: {e}")
        return None

def read_docx_file(file_path):
    logging.info(f"Reading DOCX file: {file_path}")
    try:
        doc = docx.Document(file_path)
        return " ".join([para.text for para in doc.paragraphs if para.text])
    except Exception as e:
        logging.error(f"Failed to read DOCX file: {e}")
        return None
