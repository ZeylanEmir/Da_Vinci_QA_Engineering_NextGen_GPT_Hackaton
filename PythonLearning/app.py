from dotenv import load_dotenv
import os
import streamlit as st
from clarifai.client.model import Model
import openai
from concurrent.futures import ThreadPoolExecutor
import PyPDF2

# Load API keys
load_dotenv()
clarifai_pat = os.getenv('CLARIFAI_PAT')
openai_api_key = os.getenv('OPENAI_API_KEY')

# Initialize Clarifai model
clarifai_model = Model("https://clarifai.com/openai/chat-completion/models/gpt-4-turbo")

# Set OpenAI API key
openai.api_key = openai_api_key

# Streamlit app
st.title("Chatbot with Clarifai and OpenAI GPT-4 Turbo")

# User input
user_input = st.text_input("Ask a question:")

# PDF context input
pdf_upload = st.file_uploader("Upload PDF for context:", type=["pdf"])

# Define GPT role or prompt
gpt_role_prompt = """Title: Senior QA Engineer - AI Test Automation Specialist

Responsibilities:

As a Senior QA Engineer specializing in AI test automation, your primary role is to ensure the quality and reliability of our AI-driven software solutions. You will be responsible for designing, developing, and implementing effective testing strategies to validate the functionality, performance, and security of our AI applications. Your expertise will be instrumental in establishing and maintaining robust testing processes throughout the software development lifecycle.

Key Tasks:

Test Case Design and Execution:

Develop comprehensive and detailed test cases for AI-based features and functionalities.
Collaborate with cross-functional teams to understand requirements and translate them into test scenarios.
Execute test cases manually and through automated testing tools, ensuring thorough coverage.
Unit Testing:

Create and implement unit testing strategies for AI algorithms and models.
Work closely with developers to integrate unit testing into the continuous integration (CI) pipeline.
Identify and address issues at the code level to enhance software quality.
AI Model Validation:

Collaborate with data scientists and AI engineers to validate machine learning models.
Implement testing methodologies to ensure the accuracy, efficiency, and reliability of AI algorithms.
Perform in-depth analysis of model outputs and behavior under various conditions.
Automation Framework Development:

Design and develop a scalable and maintainable test automation framework for AI applications.
Integrate test automation into the CI/CD pipeline to enable continuous testing and deployment.
Performance and Load Testing:

Conduct performance testing on AI applications to assess scalability and responsiveness.
Identify and address bottlenecks and performance issues in collaboration with development teams.
Security Testing:

Implement security testing protocols to identify vulnerabilities in AI applications.
Collaborate with security experts to ensure the resilience of AI systems against potential threats.
Test Matrix Development:

Create comprehensive test matrices outlining test coverage for different AI components.
Define testing strategies for various scenarios, including edge cases and real-world conditions.
Continuously update and optimize test matrices based on evolving project requirements.
Requirements:

Proven experience as a Senior QA Engineer with a focus on AI testing.
Strong knowledge of testing methodologies, including unit testing, integration testing, and system testing.
Expertise in developing and executing test cases for AI algorithms and models.
Proficiency in programming languages such as Python, Java, or similar for test automation.
Familiarity with AI/ML frameworks and libraries (e.g., TensorFlow, PyTorch).
Experience with version control systems (e.g., Git) and CI/CD pipelines.
Strong analytical and problem-solving skills, with an eye for detail."""

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
    inference_params = {"temperature": 0.9, "max_tokens": 1000, "api_key": openai_api_key}
    model_prediction = clarifai_model.predict_by_bytes(combined_input.encode(), input_type="text", inference_params=inference_params)
    response_text = model_prediction.outputs[0].data.text.raw

    st.text("Chatbot Response:")
    st.write(response_text)
