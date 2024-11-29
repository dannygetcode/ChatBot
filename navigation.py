# Contiene una función llamada `make_sidebar()` que se encargará de mostrar el sidebar con las opciones para "Administrador" y "Chatbot".

import streamlit as st

def configure_sidebar():
    st.sidebar.title("Navegación")

    # Botón para ir a "Inicio"
    if st.sidebar.button("Inicio"):
        st.session_state.modules = "home"

    # Botón para ir a "Administrador"
    if st.sidebar.button("Administrador"):
        st.session_state.modules = "1_login"
        

    # Botón para ir a "Chatbot"
    if st.sidebar.button("ChatBot MikhailAi"):
        st.session_state.modules = "3_chat"

    
        
        
