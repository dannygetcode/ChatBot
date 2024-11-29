# Aquí se muestran gráficos con estadísticas municipales. La página solo se debe poder acceder si el administrador está autenticado.
import streamlit as st
from navigation import configure_sidebar
from time import sleep
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

if st.session_state.get("logged_in", False):
        st.markdown("## Dashboard de Administrador")
        st.markdown("Gráfica generada para el administrador.")

        # Crear una gráfica simple con Matplotlib
        x = np.linspace(0, 10, 100)
        y = np.sin(x)

        fig, ax = plt.subplots()
        ax.plot(x, y, label="Seno")
        ax.set_title("Gráfico de Ejemplo")
        ax.set_xlabel("Eje X")
        ax.set_ylabel("Eje Y")
        ax.legend()

        # Mostrar la gráfica en Streamlit
        st.pyplot(fig)