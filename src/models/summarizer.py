# src/models/summarizer.py
from transformers import BartTokenizer, BartForConditionalGeneration
import torch
import logging
from utils.logging_utils import setup_logging

class TextSummarizer:
    def __init__(self):
        setup_logging()
        self.model_name = 'facebook/bart-large-cnn'
        try:
            self.tokenizer = BartTokenizer.from_pretrained(self.model_name)
            self.model = BartForConditionalGeneration.from_pretrained(self.model_name)
            logging.info("BART model loaded successfully.")
        except Exception as e:
            logging.error(f"Failed to load the BART model: {e}")
            raise

    def summarize(self, text):
        logging.info("Starting summarization process.")
        try:
            inputs = self.tokenizer([text], max_length=1024, return_tensors='pt', truncation=True)
            summary_ids = self.model.generate(inputs['input_ids'], max_length=150, min_length=40, length_penalty=2.0, num_beams=4, early_stopping=True)
            summary = self.tokenizer.decode(summary_ids[0], skip_special_tokens=True)
            logging.info("Summarization complete.")
            return summary
        except Exception as e:
            logging.error(f"Error during summarization: {e}")
            return "Error in summarization process."


if __name__ == "__main__":
    ts = TextSummarizer()
    test_text = "The quick brown fox jumps over the lazy dog multiple times. This sentence serves as a common typing practice text, known for containing every letter in the English alphabet."
    print("Original Text:", test_text)
    print("Summarized Text:", ts.summarize(test_text))
