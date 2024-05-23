import logging
import speech_recognition as sr
from utils.logging_utils import setup_logging

setup_logging()

def audio_to_text(audio_file):
    logging.info(f"Converting audio file to text: {audio_file}")
    recognizer = sr.Recognizer()
    try:
        with sr.AudioFile(audio_file) as source:
            audio_data = recognizer.record(source)
        return recognizer.recognize_google(audio_data)
    except sr.UnknownValueError:
        logging.warning("Audio was unclear, could not recognize.")
        return None
    except sr.RequestError as e:
        logging.error(f"API request failed: {e}")
        return None
    except Exception as e:
        logging.error(f"Unexpected error occurred: {e}")
        return None
