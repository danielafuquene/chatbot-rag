from pathlib import Path

MAX_MENSAJES = 20
_CONTEXT_FILE = Path(__file__).parent.parent / "assets" / "context.md"


def build_system_prompt(nombre_usuario: str) -> str:
    base = f"""Eres un asistente conversacional inteligente. El usuario se llama {nombre_usuario}.

Instrucciones:
- Responde en el mismo idioma que use el usuario.
- Sé claro, preciso y útil; usa ejemplos breves cuando ayuden a entender.
- Usa el historial de la conversación para mantener coherencia y recordar lo ya dicho.
- Si la pregunta es ambigua o falta información, haz una pregunta corta antes de responder.
- Si no sabes algo con certeza, dilo con honestidad en lugar de inventar.
- Para temas técnicos, estructura la respuesta con pasos o listas cuando tenga sentido."""

    extra = _load_extra_context()
    if extra:
        return f"{base}\n\nConocimiento adicional:\n{extra}"
    return base


def trim_messages(mensajes: list[dict[str, str]]) -> list[dict[str, str]]:
    if len(mensajes) <= MAX_MENSAJES:
        return mensajes
    return mensajes[-MAX_MENSAJES:]


def _load_extra_context() -> str:
    if _CONTEXT_FILE.exists():
        return _CONTEXT_FILE.read_text(encoding="utf-8").strip()
    return ""
