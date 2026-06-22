from dataclasses import dataclass
from typing import Union


@dataclass(frozen=True)
class NewChat:
    """El usuario quiere empezar una conversación vacía."""


@dataclass(frozen=True)
class SendMessage:
    """El usuario envió un mensaje de texto."""

    content: str


@dataclass(frozen=True)
class ReceiveMessage:
    """Llegó una respuesta del asistente."""

    content: str


Action = Union[NewChat, SendMessage, ReceiveMessage]
