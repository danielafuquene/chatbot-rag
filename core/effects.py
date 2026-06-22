import anthropic

_client = anthropic.Anthropic()


def fetch_assistant_reply(mensajes: list[dict[str, str]]) -> str:
    """Efecto secundario: llamada a la API externa."""
    respuesta = _client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=1000,
        messages=mensajes,
    )
    return respuesta.content[0].text
