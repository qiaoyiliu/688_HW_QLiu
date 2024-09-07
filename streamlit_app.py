import streamlit as st

hw1 = st.Page("streamlit_app_hw1.py", title="HW 1", icon = ":material/add_circle:")
hw2 = st.Page("streamlit_app_hw2.py", title="HW 2", icon=":material/add_circle:")

pg = st.navigation([hw1, hw2])
st.set_page_config(page_title="HW Manager", page_icon=":material/edit:")
pg.run()
