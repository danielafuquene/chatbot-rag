import streamlit as st


def render_profile_card(nombre_usuario: str, rol: str = "Usuario") -> None:
    st.markdown(
        f"""
        <div style="text-align: center; padding: 0.5rem 0 1.25rem 0;">
            <div style="
                width: 72px;
                height: 72px;
                margin: 0 auto 0.75rem auto;
                border-radius: 50%;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                display: flex;
                align-items: center;
                justify-content: center;
                font-size: 2rem;
            ">👤</div>
            <p style="margin: 0; font-weight: 600; font-size: 1rem;">{nombre_usuario}</p>
            <p style="margin: 0; color: #888; font-size: 0.85rem;">{rol}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
