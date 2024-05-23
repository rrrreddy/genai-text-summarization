# src/api/app.py
import gradio as gr
import logging
from models.summarizer import TextSummarizer
from services.text_input_handler import handle_text_input
from services.file_input_handler import read_text_file, read_pdf_file, read_docx_file
from services.audio_input_handler import audio_to_text
from utils.logging_utils import setup_logging

def main():
    setup_logging()
    summarizer = TextSummarizer()

    def summarize(input_type, file=None, text=None, audio=None):
        logging.info(f"Received request to summarize {input_type} input.")
        logging.info(f"File: {file}, Text: {text}, Audio: {audio}")
        try:
            if input_type == 0 and text:  # Text
                logging.info("Processing text input.")
                processed_text = handle_text_input(text)
                summary = summarizer.summarize(processed_text)
                logging.info("Text input processed successfully.")
            elif input_type in [1, 2, 3] and file:  # Text File, PDF, DOCX
                if input_type == 1:
                    logging.info(f"Processing text file: {file.name}")
                    processed_text = read_text_file(file.name)
                elif input_type == 2:
                    logging.info(f"Processing PDF file: {file.name}")
                    processed_text = read_pdf_file(file.name)
                elif input_type == 3:
                    logging.info(f"Processing DOCX file: {file.name}")
                    processed_text = read_docx_file(file.name)
                
                if processed_text:
                    summary = summarizer.summarize(processed_text)
                    logging.info(f"{['Text File', 'PDF', 'DOCX'][input_type-1]} processed successfully.")
                else:
                    summary = "Failed to process the file. Check logs for more details."
                    logging.error(f"Failed to process {['Text File', 'PDF', 'DOCX'][input_type-1]}: {file.name}")
            elif input_type == 4:
                if audio:
                    logging.info("Processing recorded audio.")
                    processed_text = audio_to_text(audio)
                elif file:
                    logging.info(f"Processing uploaded audio file: {file.name}")
                    processed_text = audio_to_text(file.name)
                else:
                    processed_text = None
                
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
            gr.Radio(
                choices=['Text', 'Text File', 'PDF', 'DOCX', 'Audio'], 
                label="Select Input Type", 
                type="index",
                interactive=True
            ),
            gr.File(label="Upload a file"),
            gr.Textbox(label="Or enter text here", placeholder="Type your text here..."),
            gr.Audio(type="filepath", label="Or record audio here")
        ],
        outputs=gr.Textbox(label="Summarized Text", placeholder="The summary will appear here..."),
        title="GenAI Text Summarizer",
        description="Upload a text file, a PDF, a DOCX, an audio file, or type in text to summarize. Select the appropriate input type and provide the input.",
        theme="huggingface",  # Apply a Hugging Face theme for a modern look
        allow_flagging="never"  # Disable flagging for simplicity
    )

    iface.launch()


if __name__ == "__main__":
    logging.info(f"Starting GenAI Text Summarizer.")
    main()
    logging.info(f"Closing GenAI Text Summarizer.")
    
