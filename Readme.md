# QA Engineer Assistant Chatbot

Welcome to the QA Engineer Assistant Chatbot repository! This project is designed to assist QA Engineers in creating test cases and enhancing their testing workflow through an AI-driven chatbot. The chatbot is built using OpenAI's GPT-4 Turbo and Clarifai's language model.

## Installation

1. **Clone the repository to your local machine:**
    ```bash
    git clone https://github.com/your-username/QA-Engineer-Assistant.git
    cd QA-Engineer-Assistant
    ```

2. **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3. **Create a virtual environment (optional but recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use 'venv\Scripts\activate'
    ```

4. **Set up API keys:**
    - Obtain Clarifai API key and OpenAI API key.
    - Create a `.env` file in the project root and add the keys:
        ```plaintext
        CLARIFAI_PAT=your_clarifai_api_key
        OPENAI_API_KEY=your_openai_api_key
        ```

## Usage

1. **Run the Streamlit app:**
    ```bash
    streamlit run qa_engineer_assistant.py
    ```

2. **Access the app in your web browser at [http://localhost:8501](http://localhost:8501).**

3. **Ask a question in the provided text input.**

4. **Optionally, upload a PDF file to provide additional context for the chatbot.**

5. **The chatbot will generate a response based on your question and the provided context.**

## Project Details

### Files and Structure

- `qa_engineer_assistant.py`: Streamlit app script for the QA Engineer Assistant Chatbot.
- `requirements.txt`: List of Python dependencies required for the project.
- `README.md`: Project documentation.

### Dependencies

- Streamlit: UI framework for creating web applications with Python.
- Clarifai: Python client for interacting with the Clarifai language model.
- OpenAI: Python client for interfacing with the GPT-4 Turbo language model.
- PyPDF2: Library for working with PDF files in Python.

### Project Workflow

1. User inputs a question related to QA engineering in the Streamlit app.
2. Optionally, the user can upload a PDF document to provide additional context.
3. The app combines the user input, predefined QA engineer role prompt, and PDF content.
4. The combined input is sent to the Clarifai GPT-4 Turbo model for generating a response.
5. The generated response is displayed in the Streamlit app.

## Contributors

- Emir Zeylan (@ZeylanEmir)
- Izmukhanov Daniyar (https://t.me/kazakh1488)

Feel free to contribute, report issues, or suggest improvements. Happy testing! 🚀
