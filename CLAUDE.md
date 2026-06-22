# Guía del proyecto para Claude

## Arquitectura

Este proyecto usa **MVU** (Model-View-Update) con esta estructura:

```
chat_app.py          → punto de entrada
core/                → lógica (models, actions, update, effects, state, prompts)
components/          → UI reutilizable (sidebar, profile_card, chat_messages)
features/            → pantallas completas (features/chat/screen.py)
assets/              → archivos estáticos y contexto
```

## Convenciones de código

- Python 3.9+, tipos en funciones públicas.
- La UI no debe mutar estado directamente; usar `actions` + `update`.
- Efectos externos (API, archivos) solo en `core/effects.py`.
- No commitear secretos: `.env` debe estar en `.gitignore`.
- Comentarios solo cuando la lógica no sea obvia.
- Mantener cambios pequeños y enfocados.

## Code review: qué revisar

1. **Arquitectura**: ¿el código está en la carpeta correcta (`core` vs `components` vs `features`)?
2. **MVU**: ¿las transiciones de estado son puras en `update.py`?
3. **Seguridad**: ¿hay API keys, tokens o datos sensibles hardcodeados?
4. **Streamlit**: ¿`session_state` se gestiona solo en `core/state.py`?
5. **Errores**: ¿faltan validaciones en inputs del usuario o llamadas a la API?
6. **Claridad**: ¿nombres y funciones son legibles sin sobre-ingeniería?

## Respuestas del revisor

- Escribir el review en **español**.
- Ser constructivo: explicar el problema y sugerir una mejora concreta.
- Priorizar bugs y seguridad sobre estilo menor.
