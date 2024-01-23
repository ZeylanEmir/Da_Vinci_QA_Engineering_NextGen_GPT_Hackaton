from dotenv import load_dotenv
import os
import streamlit as st
import openai
from concurrent.futures import ThreadPoolExecutor
import PyPDF2

# Load dotenv file
load_dotenv()

# Streamlit app
st.title("AI QA Engineering Assistant")

# User input for OpenAI API key
openai_api_key = st.text_input("Enter your OpenAI API key:", type="password")

# Set OpenAI API key
openai.api_key = openai_api_key

# User input
user_input = st.text_input("Ask a question:", key="question_input")

# PDF context input
pdf_upload = st.file_uploader("Upload PDF for context:", type=["pdf"], key="pdf_upload")

# Define GPT role or prompt
gpt_role_prompt = """Make pretty and simple matrix test cases for application or sites like Senior QA Engineer"""

# Function for processing PDF content
def process_pdf_content(pdf_file):
    pdf_text = ""
    try:
        with pdf_file as file:
            pdf_reader = PyPDF2.PdfFileReader(file)
            for page_num in range(pdf_reader.numPages):
                page = pdf_reader.getPage(page_num).extractText()
                pdf_text += page
    except Exception as e:
        st.error(f"Error processing PDF: {e}")
    return pdf_text

# Combine user input and PDF context with GPT role or prompt
combined_input = f"{gpt_role_prompt}{user_input} "

# Model Predict
if pdf_upload:
    with ThreadPoolExecutor() as executor:
        # Process PDF content asynchronously
        future = executor.submit(process_pdf_content, pdf_upload)
        context_text = future.result()

        # Combine user input and processed PDF context
        combined_input += context_text

if combined_input.strip():
    inference_params = {"temperature": 1, "max_tokens": 1000, "api_key": openai_api_key}
    model_prediction = openai.Completion.create(
        engine="davinci-codex",
        prompt=combined_input,
        temperature=inference_params["temperature"],
        max_tokens=inference_params["max_tokens"]
    )
    response_text = model_prediction.choices[0].text

    st.text("Chatbot Response:")
    st.write(response_text)
