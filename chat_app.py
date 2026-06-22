import streamlit as st
import anthropic
from dotenv import load_dotenv

# Carga la API key desde el archivo .env
load_dotenv()

# Título de la página
st.title("🤖 Mi Chatbot con Claude")

# Crea el cliente de Anthropic (se conecta usando tu API key)
client = anthropic.Anthropic()

# Inicializa el historial de chat en la "memoria" de la sesión
# Esto es necesario porque Streamlit recarga todo el script en cada interacción
if "mensajes" not in st.session_state:
    st.session_state.mensajes = []

# Muestra el historial de mensajes anteriores
for mensaje in st.session_state.mensajes:
    with st.chat_message(mensaje["role"]):
        st.markdown(mensaje["content"])

# Caja de entrada para que el usuario escriba
pregunta_usuario = st.chat_input("Escribe tu mensaje...")

if pregunta_usuario:
    # Guarda y muestra el mensaje del usuario
    st.session_state.mensajes.append({"role": "user", "content": pregunta_usuario})
    with st.chat_message("user"):
        st.markdown(pregunta_usuario)

    # Llama a la API de Claude con todo el historial de la conversación
    with st.chat_message("assistant"):
        with st.spinner("Pensando..."):
            respuesta = client.messages.create(
                model="claude-sonnet-4-6",
                max_tokens=1000,
                messages=st.session_state.mensajes
            )
            texto_respuesta = respuesta.content[0].text
            st.markdown(texto_respuesta)

    # Guarda la respuesta de Claude en el historial
    st.session_state.mensajes.append({"role": "assistant", "content": texto_respuesta})