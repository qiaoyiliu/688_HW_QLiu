import streamlit as st
import importlib
import sys
#from openai import OpenAI
#from anthropic import Anthropic
#from anthropic.types.message import Message

st.set_page_config(page_title="HW Manager", page_icon=":material/edit:")
st.sidebar.title("Navigation")
selected_page = st.sidebar.radio("Select Homework", ["HW 1", "HW 2", "test"])

st.sidebar.title("LLM Options")
#llm_options = ['gpt-4o-mini', 'Claude 3 Opus']
selected_llm = st.sidebar.radio("Choose LLM to use:", 
                                ['gpt-4o-mini', 'claude-3-haiku-20240307', 'mistral-small-latest'])

if selected_page == "HW 1":
    if 'streamlit_app_hw1' in sys.modules:
        hw1 = sys.modules['streamlit_app_hw1']
        importlib.reload(hw1)
    else:
        hw1 = importlib.import_module("streamlit_app_hw1")
    
    hw1.display(selected_llm)

elif selected_page == "HW 2":
    if 'streamlit_app_hw2' in sys.modules:
        hw2 = sys.modules['streamlit_app_hw2']
        importlib.reload(hw2)
    else:
        hw2 = importlib.import_module("streamlit_app_hw2")
    
    hw2.display(selected_llm)

elif selected_page == "test":
    st.write(f"You have selected LLM: {selected_llm}")



#st.sidebar.title("LLM Options")
#llm_options = ['gpt-4o-mini']
#selected_llm = st.sidebar.selectbox("Choose LLM to use:", llm_options)
#pg = st.navigation([hw1, hw2])

#st.set_page_config(page_title="HW Manager", page_icon=":material/edit:")
#pg.run()



#if selected_llm == 'gpt-4o-mini':
    #openai_api_key = st.secrets["OPENAI_API_KEY"]
    #client = OpenAI(api_key = openai_api_key)
#   client = OpenAI(api_key = "OPENAI_API_KEY")
#elif selected_llm == 'Claude 3 Opus':
#    anthropic_api_key = st.secrets["ANTHROPIC_API_KEY"]
#    client = Anthropic(api_key=anthropic_api_key)

#    response: Message = client.messages.create(
#        max_tokens= 256,
#        messages= [{'role':'user', 'content': 'Hello!'}],
#        model = "claude-3-opus-20240229",
#        temperature=0.5
#    )

#    answer = response.content[0].text
#    print(answer)




#pg = st.navigation(["HW 1", "HW 2"])
#pg.run()

#hw1 = st.Page("streamlit_app_hw1.py", title="HW 1", icon = ":material/add_circle:")
#hw2 = st.Page("streamlit_app_hw2.py", title="HW 2", icon=":material/add_circle:")

#if selected_page == "HW 1":
    #st.write(f"You have selected LLM: {selected_llm}")
#    if 'streamlit_app_hw1' in sys.modules:
#        importlib.reload(sys.modules['streamlit_app_hw1'])
#        hw1 = sys.modules['streamlit_app_hw1']
#    else:
#        hw1 = importlib.import_module("streamlit_app_hw1")
#    hw1.display(selected_llm)
#elif selected_page == "HW 2":
    #st.write(f"You have selected LLM: {selected_llm}")
#    if 'streamlit_app_hw2' in sys.modules:
#        importlib.reload(sys.modules['streamlit_app_hw2'])
#        hw2 = sys.modules['streamlit_app_hw2']
#    else:
#        hw2 = importlib.import_module("streamlit_app_hw2")
#    hw2.display(selected_llm)
#elif selected_page =="test":
#    st.write(f"You have selected LLM: {selected_llm}")
    #test.display(selected_llm)

#------------------------    