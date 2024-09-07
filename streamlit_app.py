import streamlit as st
import importlib
from openai import OpenAI
from anthropic import Anthropic
from anthropic.types.message import Message

st.set_page_config(page_title="HW Manager", page_icon=":material/edit:")

st.sidebar.title("Navigation")
selected_page = st.sidebar.radio("Select Homework", ["HW 1", "HW 2", "test"])

st.sidebar.title("LLM Options")
llm_options = ['gpt-4o-mini', 'Claude 3 Opus']
selected_llm = st.sidebar.selectbox("Choose LLM to use:", llm_options)

if selected_llm == 'gpt-4o-mini':
    #openai_api_key = st.secrets["OPENAI_API_KEY"]
    #client = OpenAI(api_key = openai_api_key)
    client = OpenAI(api_key = "OPENAI_API_KEY")
elif selected_llm == 'Claude 3 Opus':
    anthropic_api_key = st.secrets["ANTHROPIC_API_KEY"]
    client = Anthropic(api_key=anthropic_api_key)

    response: Message = client.messages.create(
        max_tokens= 256,
        messages= [{'role':'user', 'content': 'Hello!'}],
        model = "claude-3-opus-20240229",
        temperature=0.5
    )

    answer = response.content[0].text
    print(answer)

if selected_page == "HW 1":
    st.write(f"You have selected LLM: {selected_llm}")
    hw1 = importlib.import_module("streamlit_app_hw1")
elif selected_page == "HW 2":
    st.write(f"You have selected LLM: {selected_llm}")
    hw2 = importlib.import_module("streamlit_app_hw2")
elif selected_page =="test":
    st.write(f"You have selected LLM: {selected_llm}")
    


#import streamlit as st

#hw1 = st.Page("streamlit_app_hw1.py", title="HW 1", icon = ":material/add_circle:")
#hw2 = st.Page("streamlit_app_hw2.py", title="HW 2", icon=":material/add_circle:")

#st.sidebar.title("LLM Options")
#llm_options = ['gpt-4o-mini']
#selected_llm = st.sidebar.selectbox("Choose LLM to use:", llm_options)
#pg = st.navigation([hw1, hw2])

#st.set_page_config(page_title="HW Manager", page_icon=":material/edit:")
#pg.run()
