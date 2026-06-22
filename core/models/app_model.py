from dataclasses import dataclass, field


@dataclass
class AppModel:
    """Estado completo de la aplicación."""

    mensajes: list[dict[str, str]] = field(default_factory=list)
    nombre_usuario: str = "Daniela"
