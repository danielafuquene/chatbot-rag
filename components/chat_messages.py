import streamlit as st


def render_chat_messages(mensajes: list[dict[str, str]]) -> None:
    for mensaje in mensajes:
        with st.chat_message(mensaje["role"]):
            st.markdown(mensaje["content"])
