import anthropic

from core.prompts import build_system_prompt, trim_messages

_client = anthropic.Anthropic()


def fetch_assistant_reply(
    mensajes: list[dict[str, str]],
    nombre_usuario: str = "Usuario",
) -> str:
    """Efecto secundario: llamada a la API con system prompt y contexto recortado."""
    respuesta = _client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=2048,
        system=build_system_prompt(nombre_usuario),
        messages=trim_messages(mensajes),
    )
    return respuesta.content[0].text
