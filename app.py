import streamlit as st

# Título de la app
st.title("Mi primera app en Streamlit 🚀")

# Texto descriptivo
st.write("Esta es una app simple para entender los componentes básicos.")

# Input de texto: el usuario escribe su nombre
nombre = st.text_input("¿Cuál es tu nombre?")

# Slider: el usuario elige un número
edad = st.slider("¿Cuál es tu edad?", 0, 100, 25)

# Botón
if st.button("Saludar"):
    if nombre:
        st.success(f"¡Hola {nombre}! Tienes {edad} años.")
    else:
        st.warning("Por favor escribe tu nombre primero.")

# Un selector de opciones
opcion = st.selectbox(
    "¿Qué área de IA te interesa más?",
    ["Chatbots / LLMs", "Visión por computadora", "Análisis de datos", "Audio"]
)

st.write(f"Elegiste: **{opcion}**")