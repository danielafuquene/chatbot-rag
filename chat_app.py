import streamlit as st
from dotenv import load_dotenv

from features.chat.screen import run_chat_screen

load_dotenv()

st.set_page_config(
    page_title="Chatbot con Claude",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
)

run_chat_screen()
