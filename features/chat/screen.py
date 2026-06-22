import streamlit as st

from components.chat_messages import render_chat_messages
from components.sidebar import render_sidebar
from core.actions import ReceiveMessage, SendMessage
from core.effects import fetch_assistant_reply
from core.models.app_model import AppModel
from core.state import get_model, set_model
from core.update import needs_reply, update


def run_chat_screen() -> None:
    model = get_model()

    sidebar_action = render_sidebar(model)
    if sidebar_action is not None:
        set_model(update(model, sidebar_action))
        st.rerun()

    st.title("🤖 Mi Chatbot con Claude")
    render_chat_messages(model.mensajes)

    if needs_reply(model):
        _fetch_and_store_reply(model)
        return

    pregunta_usuario = st.chat_input(
        "Escribe tu mensaje...",
        disabled=needs_reply(model),
    )
    if pregunta_usuario:
        set_model(update(model, SendMessage(pregunta_usuario)))
        st.rerun()


def _fetch_and_store_reply(model: AppModel) -> None:
    with st.chat_message("assistant"):
        with st.spinner("Pensando..."):
            texto_respuesta = fetch_assistant_reply(
                model.mensajes,
                nombre_usuario=model.nombre_usuario,
            )
    set_model(update(model, ReceiveMessage(texto_respuesta)))
    st.rerun()
