# Esta pagina contiene la interfaz de inicio de sesión para el administrador. Si el usuario ingresa credenciales correctas, redirige a `2_charts.py` donde se muestran las estadísticas.


import streamlit as st
from time import sleep
from navigation import make_sidebar

make_sidebar()


username = st.text_input("Username")
password = st.text_input("Password", type="password")

if st.button("Iniciar Sesión", type="primary"):
    if username == "admin" and password == "123":
        st.session_state.logged_in = True
        st.success("Sesión iniciado con éxito!")
        sleep(0.5)
        st.switch_page("modules/2_charts.py")
    else:
        st.error("Incorrecto el usuario o contraseña")
