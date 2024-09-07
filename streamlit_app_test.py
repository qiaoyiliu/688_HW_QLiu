import streamlit as st

def display(llm):
    # Ensure that the page content is always rendered when this function is called
    st.set_page_config(page_title="test", page_icon=":material/add_circle:")
    st.title("Joy's Document Question Answering for HW1")
    st.write(
        "Upload a document below and ask a question about it – GPT will answer! "
        "To use this app, you need to provide an OpenAI API key, which you can get [here](https://platform.openai.com/account/api-keys)."
    )

    languages = ['English', 'Spanish', 'French']
    selected_language = st.selectbox('Select your language:', languages)
    st.write(f"You have selected: {selected_language}")

    # OpenAI API Key
    openai_api_key = st.text_input("OpenAI API Key", type="password")
    if not openai_api_key:
        st.info("Please add your OpenAI API key to continue.", icon="🗝️")
        return

    # Create an OpenAI client.
    client = OpenAI(api_key=openai_api_key)

    # File upload logic
    uploaded_file = st.file_uploader("Upload a document (.txt, or .pdf)", type=("txt", "pdf"))
    question_url = st.text_area("Please insert a URL:", placeholder="")
    question = st.text_area(
        "Now ask a question about the document!",
        placeholder="Can you give me a short summary?",
        disabled=not uploaded_file,
    )

    if uploaded_file and question:
        file_extension = uploaded_file.name.split('.')[-1]
        if file_extension == 'txt':
            document = uploaded_file.read().decode()
        elif file_extension == 'pdf':
            document = read_pdf(uploaded_file)
        else:
            st.error("Unsupported file type.")
            return

        messages = [
            {
                "role": "user",
                "content": f"Respond in {selected_language}. Here's a document: {document} \n\n---\n\n {question}",
            }
        ]

        # Generate an answer using the OpenAI API with the selected LLM, temperature, and max tokens
        stream = client.chat.completions.create(
            model=llm,  # Use the selected LLM
            messages=messages,
            stream=True,
            temperature=temperature,
            max_tokens=max_tokens
        )

        # Stream the response to the app
        st.write_stream(stream)
