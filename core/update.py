from core.actions import Action, NewChat, ReceiveMessage, SendMessage
from core.models.app_model import AppModel


def update(model: AppModel, action: Action) -> AppModel:
    """Transición pura: recibe estado + acción y devuelve el nuevo estado."""
    if isinstance(action, NewChat):
        return AppModel(nombre_usuario=model.nombre_usuario)

    if isinstance(action, SendMessage):
        return AppModel(
            mensajes=model.mensajes + [{"role": "user", "content": action.content}],
            nombre_usuario=model.nombre_usuario,
        )

    if isinstance(action, ReceiveMessage):
        return AppModel(
            mensajes=model.mensajes + [{"role": "assistant", "content": action.content}],
            nombre_usuario=model.nombre_usuario,
        )

    return model


def needs_reply(model: AppModel) -> bool:
    """True si el último mensaje es del usuario y aún no hay respuesta."""
    return bool(model.mensajes) and model.mensajes[-1]["role"] == "user"
