import gradio as gr
import logging
from models.summarizer import TextSummarizer
from services.text_input_handler import handle_text_input
from services.file_input_handler import read_text_file, read_pdf_file, read_docx_file
from services.audio_input_handler import audio_to_text
from utils.logging_utils import setup_logging

setup_logging()
summarizer = TextSummarizer()

def summarize(input_type, file=None, text=None):
    logging.info(f"Received request to summarize {input_type} input.")
    try:
        if input_type == 'Text' and text:
            logging.info("Processing text input.")
            processed_text = handle_text_input(text)
            summary = summarizer.summarize(processed_text)
            logging.info("Text input processed successfully.")
        elif input_type in ['PDF', 'DOCX', 'Text File'] and file:
            if input_type == 'PDF':
                logging.info(f"Processing PDF file: {file.name}")
                processed_text = read_pdf_file(file.name)
            elif input_type == 'DOCX':
                logging.info(f"Processing DOCX file: {file.name}")
                processed_text = read_docx_file(file.name)
            elif input_type == 'Text File':
                logging.info(f"Processing text file: {file.name}")
                processed_text = read_text_file(file.name)
            
            if processed_text:
                summary = summarizer.summarize(processed_text)
                logging.info(f"{input_type} file processed successfully.")
            else:
                summary = "Failed to process the file. Check logs for more details."
                logging.error(f"Failed to process {input_type} file: {file.name}")
        elif input_type == 'Audio' and file:
            logging.info(f"Processing audio file: {file.name}")
            processed_text = audio_to_text(file.name)
            if processed_text:
                summary = summarizer.summarize(processed_text)
                logging.info("Audio input processed successfully.")
            else:
                summary = "Failed to convert audio to text. Check logs for more details."
                logging.error("Failed to convert audio to text.")
        else:
            summary = "Invalid input. Please provide a valid file or text."
            logging.warning("Invalid input type provided.")
        
        return summary
    except Exception as e:
        logging.error(f"Error during summarization: {e}")
        return "An error occurred during summarization. Please check the logs for more details."

iface = gr.Interface(
    fn=summarize,
    inputs=[
        gr.Radio(choices=['Text', 'Text File', 'PDF', 'DOCX', 'Audio'], label="Select Input Type"),
        gr.File(label="Upload a file", optional=True),
        gr.Textbox(label="Or enter text here", optional=True)
    ],
    outputs=gr.Textbox(label="Summarized Text"),
    title="GenAI Text Summarizer",
    description="Upload a text file, a PDF, a DOCX, or an audio file, or just type in text to summarize."
)

if __name__ == "__main__":
    logging.info("Starting Gradio interface.")
    iface.launch()
    logging.info("Gradio interface stopped.")
