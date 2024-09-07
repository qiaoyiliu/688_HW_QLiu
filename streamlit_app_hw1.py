import streamlit as st
import PyPDF2
import pdfplumber
from openai import OpenAI
from anthropic import Anthropic
from anthropic.types.message import Message
import google.generativeai as genai

# Show title and description.
st.title("Joy's Document question answering for HW1")
st.write(
    "Upload a document below and ask a question about it – GPT will answer! "
    "To use this app, you need to provide an OpenAI API key, which you can get [here](https://platform.openai.com/account/api-keys). "
)

def read_pdf(pdf_file):
    reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in range(len(reader.pages)):
        text += reader.pages[page].extract_text()
    return text

def display(selected_llm):
    client = None

    if selected_llm == 'gpt-4o-mini':
        api_key = st.text_input("OpenAI API Key", type="password")
        if api_key:
            client = OpenAI(api_key=api_key)
        else:
            st.warning("Please provide OpenAI API key")
            return
    elif selected_llm == 'Claude 3 Opus':
        api_key = st.text_input("Anthropic API Key", type="password")
        if api_key:
            client = Anthropic(api_key=api_key)
        else:
            st.warning("Please provide Anthropic API key")
            return
    #else: 
        #st.info("Please add your OpenAI API key to continue.", icon="🗝️")

    #ask user to upload file
    uploaded_file = st.file_uploader(
        "Upload a document (.txt, or .pdf)", type=("txt", "pdf")
    )

    #or ask user to paster URL
    question_url = st.text_area(
        "Or insert an URL:",
        placeholder="Copy URL here",
    )

    #ask user to select language
    languages = ['English', 'Spanish', 'French']
    selected_language = st.selectbox('Select your language:', languages)
    st.write(f"You have selected: {selected_language}")


    question = st.text_area(
        "Now ask a question about the document!",
        placeholder="Can you give me a short summary?",
        disabled=not uploaded_file,
    )

    if client is None:
        st.info("Please enter API key to continue.")
    else:
        if uploaded_file and question:
            file_extension = uploaded_file.name.split('.')[-1]
            if file_extension == 'txt':
                document = uploaded_file.read().decode()
            elif file_extension == 'pdf':
                document = read_pdf(uploaded_file)
            else:
                st.error("Unsupported file type.")
            messages = [
                {
                    "role": "user",
                    "content": f"Respond in {selected_language}. Here's a document: {document} \n\n---\n\n {question}",
                }
            ]
            stream = client.chat.completions.create(
            model=selected_llm,
            messages=messages,
            stream=True
            )
            st.write_stream(stream)

# Ask user for their OpenAI API key via `st.text_input`.
# Alternatively, you can store the API key in `./.streamlit/secrets.toml` and access it
# via `st.secrets`, see https://docs.streamlit.io/develop/concepts/connections/secrets-management
#openai_api_key = st.text_input("OpenAI API Key", type="password")
#if not openai_api_key:
#    st.info("Please add your OpenAI API key to continue.", icon="🗝️")
#else:

    # Create an OpenAI client.
#    client = OpenAI(api_key=openai_api_key)

    # Let the user upload a file via `st.file_uploader`.
#    uploaded_file = st.file_uploader(
#        "Upload a document (.txt or .pdf)", type=("txt", "pdf")
#    )

    # Ask the user for a question via `st.text_area`.
#    question = st.text_area(
#        "Now ask a question about the document!",
#        placeholder="Can you give me a short summary?",
#        disabled=not uploaded_file,
#    )

#    if uploaded_file and question:

        # Process the uploaded file and question.
#        file_extension = uploaded_file.name.split('.')[-1]
#        if file_extension == 'txt':
#          document = uploaded_file.read().decode()
#        elif file_extension == 'pdf':
#          document = read_pdf(uploaded_file)
#        else:
#          st.error("Unsupported file type.")
#        messages = [
#            {
#                "role": "user",
#                "content": f"Here's a document: {document} \n\n---\n\n {question}",
#            }
#        ]

        # Generate an answer using the OpenAI API.
#        stream = client.chat.completions.create(
#            model="gpt-4o-mini",
#            messages=messages,
#            stream=True,
#        )

        # Stream the response to the app using `st.write_stream`.
#        st.write_stream(stream)
