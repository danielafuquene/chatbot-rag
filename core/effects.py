import anthropic
from features.knowledge.search import buscar_contexto

from core.prompts import build_system_prompt, trim_messages
from dotenv import load_dotenv



#_client = anthropic.Anthropic()
import os

print("KEY:", os.getenv("ANTHROPIC_API_KEY"))
load_dotenv()
client = anthropic.Anthropic(
    api_key=os.getenv("ANTHROPIC_API_KEY")
)
_client = anthropic.Anthropic(
    api_key=os.getenv("ANTHROPIC_API_KEY")
)

print("CLIENTE CREADO")


def fetch_assistant_reply(
    mensajes: list[dict[str, str]],
    nombre_usuario: str = "Usuario",
) -> str:

    # Última pregunta del usuario
    pregunta = mensajes[-1]["content"]

    # PASO 4
    contexto = buscar_contexto(pregunta)

    system_prompt = f"""
    {build_system_prompt(nombre_usuario)}

    Contexto encontrado en la base de conocimiento:

    {contexto}

    Utiliza esta información para responder cuando sea relevante.
    """

    respuesta = _client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=2048,
        system=system_prompt,
        messages=trim_messages(mensajes),
    )

    return respuesta.content[0].text
