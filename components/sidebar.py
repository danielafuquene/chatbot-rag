from typing import Optional

import streamlit as st

from components.profile_card import render_profile_card
from core.actions import Action, NewChat
from core.models.app_model import AppModel


def render_sidebar(model: AppModel) -> Optional[Action]:
    with st.sidebar:
        render_profile_card(model.nombre_usuario)
        st.divider()

        if st.button("➕ Nuevo chat", use_container_width=True, type="primary"):
            return NewChat()

    return None
