import streamlit as st
from openai import OpenAI
import requests
from bs4 import BeautifulSoup
import time
import os
import logging
import openai
from openai import AzureOpenAI


def read_url_content(url):
   try:
      response=requests.get(url)
      response.raise_for_status() 
      soup=BeautifulSoup(response.content, 'html.parser')
      return soup.get_text()
   except requests.RequestException as e:
      print(f"Error reading {url}:{e}")
      return None

# Show title and description.
st.title("Joy's Document question answering for HW1")
st.write(
    "Upload a document below and ask a question about it – GPT will answer! "
    "To use this app, you need to provide an OpenAI API key, which you can get [here](https://platform.openai.com/account/api-keys). "
)

languages = ['English', 'Spanish', 'French']
selected_language = st.selectbox('Select your language:', languages)
st.write(f"You have selected: {selected_language}")

# Ask user for their OpenAI API key via `st.text_input`.
# Alternatively, you can store the API key in `./.streamlit/secrets.toml` and access it
# via `st.secrets`, see https://docs.streamlit.io/develop/concepts/connections/secrets-management
openai_api_key = st.text_input("OpenAI API Key", type="password")
#openai_api_key = st.secrets["OPENAI_API"]
if not openai_api_key:
    st.info("Please add your OpenAI API key to continue.", icon="🗝️")
else:

    # Create an OpenAI client.
    client = OpenAI(api_key=openai_api_key)

    # Let the user upload a file via `st.file_uploader`.
    uploaded_file = st.file_uploader(
        "Upload a document (.txt, or .pdf)", type=("txt", "pdf")
    )

    question_url = st.text_area(
       "Please insert an URL:",
       placeholder="",
    )

    # Ask the user for a question via `st.text_area`.
    question = st.text_area(
        "Now ask a question about the document!",
        placeholder="Can you give me a short summary?",
        disabled=not uploaded_file,
    )

    if uploaded_file and question:

        # Process the uploaded file and question.
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

        # Generate an answer using the OpenAI API.
        stream = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
            stream=True,
        )


        # Stream the response to the app using `st.write_stream`.
        st.write_stream(stream)

    else:
       url_content = read_url_content(question_url)
       messages = [
            {
                "role": "user",
                "content": f"Respond in {selected_language}. Here's a URL: {url_content} \n\n---\n\n {question}",
            }
        ]
       
       stream = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
            stream=True,
        )
       
       st.write_stream(stream)
       


question_to_ask = "Why are LLMs (AI) a danger to society?"
system_message = """
Goal: Answer the question using bullets. 
      The answer should be appropriate for a 10 year old child to understand
"""
def output_info(content, start_time, model_info):
   end_time = time.time()
   time_taken = end_time - start_time
   time_taken = round(time_taken * 10)/10

   output = f"For {model_info}, time taken = " + str(time_taken)
   logging.info(output)
   logging.info(f"  --> {content}")

   str.write(output)

def do_openAI(model):
   client = AzureOpenAI(
      api_version=openai.api_version,
      azure_endpoint=openai.api_base,
      api_key=openai_api_key
   )
   
   message_to_LLM = [
      {"role":"system", "content":system_message},
      {"role":"user", "content":question_to_ask}
   ]

   completion = client.chat.completions.create(
      model = "gpt-4o-mini",
      messages=message_to_LLM,
      temperature=0,
      seed=10,
      max_tokens=1500,
      stream=True
   ) 

   content = ""
   