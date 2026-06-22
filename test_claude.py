import os
from dotenv import load_dotenv
import anthropic

# Carga las variables del archivo .env
load_dotenv()

# Crea el cliente conectado a tu API key
client = anthropic.Anthropic()

# Envía un mensaje simple de prueba
mensaje = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=200,
    messages=[
        {"role": "user", "content": "Hola Claude, ¿estás funcionando?"}
    ]
)

print(mensaje.content[0].text)