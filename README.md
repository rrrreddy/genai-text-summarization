# Project Documentation
# GenAI Text Summarizer

## Overview

GenAI Text Summarizer is a powerful and flexible text summarization tool that leverages generative AI models. The application allows users to input text through various methods, including typing, file uploads (PDF, DOCX, text files), and audio recordings, and generates concise summaries of the input content. This project is designed with a modular structure to ensure scalability and ease of maintenance.

## Features

- **Text Input**: Enter text directly into the application for summarization.
- **File Upload**: Upload text files, PDF documents, or DOCX files for summarization.
- **Audio Input**: Record or upload audio files which are transcribed and summarized.
- **User-Friendly Interface**: An intuitive web interface powered by Gradio for easy interaction.

## Installation

### Prerequisites

- Python 3.11 or higher
- Virtual environment (optional but recommended)

### Steps

1. **Clone the Repository**

    ```bash
    git clone https://github.com/rrrreddy/genai-text-summarization.git
    cd genai-text-summarization
    ```

2. **Create and Activate a Virtual Environment**

    ```bash
    python -m venv .env
    source .env/bin/activate  # On Windows use `.env\Scripts\activate`
    ```

3. **Install the Dependencies**

    ```bash
    pip install -r requirements.txt
    ```

4. **Install the Package**

    ```bash
    pip install -e .
    ```

## Usage

To start the application, run the following command:

```bash
genai-text-summarizer
```

Alternatively, you can run it as a Python module:

python -m api.app

### Interface
Once the application is running, open your web browser and navigate to the provided URL (typically http://127.0.0.1:7860). You will see an interface with the following options:

* Select Input Type: Choose the type of input you want to summarize (Text, Text File, PDF, DOCX,Audio).
* Upload a File: If you selected a file type, upload the respective file here.
* Or Enter Text Here: If you selected text, enter it directly into the textbox.
* Or Record Audio Here: If you selected audio, you can record audio directly from your microphone.
* Click the Submit button to generate a summary of the provided input.

### Description of Key Files and Directories
* src/: Contains the main source code for the application.
* api/: Contains the main application entry point and API logic.
* models/: Contains the summarization model logic.
* services/: Contains the input handling logic for different types of inputs.
* utils/: Contains utility functions, such as logging setup.
* notebooks/: Contains Jupyter notebooks for experiments and examples.
* tests/: Contains test cases for the application.

## Logging
Logs are written to logs/app.log in the project directory. Ensure you check this file for detailed logs and debugging information.

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request for any improvements or bug fixes.

## Acknowledgments
- Thanks to the Hugging Face team for providing amazing tools and models.
- Gradio for their intuitive interface framework.