import streamlit as st

from core.models.app_model import AppModel


def get_model() -> AppModel:
    if "model" not in st.session_state:
        st.session_state.model = AppModel()
    return st.session_state.model


def set_model(model: AppModel) -> None:
    st.session_state.model = model
