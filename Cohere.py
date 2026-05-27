import streamlit as st
import cohere
import os
from dotenv import load_dotenv

# 1. Cargamos el archivo .env para desarrollo local
load_dotenv()

# 2. Obtenemos la API KEY de forma segura:
# Primero busca en los Secrets de Streamlit, si no lo encuentra, busca en el .env local
api_key = st.secrets.get("COHERE_API_KEY") or os.getenv("COHERE_API_KEY")

# 3. Inicializamos el cliente de Cohere
client = None
if api_key:
    client = cohere.Client(api_key=api_key)

# --- Configuración de la Interfaz con Streamlit ---
st.set_page_config(page_title="Asistente IA", page_icon="🤖")

st.title("🚀 Generador de Ideas con Cohere")
st.markdown("Introduce un tema para obtener sugerencias creativas utilizando Inteligencia Artificial.")

# Campo de entrada de texto
tema_usuario = st.text_input("¿Sobre qué quieres generar ideas?", "Programación en Python")

if st.button("Generar Ideas"):
    if not api_key:
        st.error("Error: No se encontró la API KEY de Cohere. Configúrala en los Secrets de Streamlit.")
    elif not client:
        st.error("Error: No se pudo inicializar el cliente de Cohere.")
    else:
        with st.spinner("Consultando a Cohere..."):
            try:
                # 4. Generamos el contenido usando el cliente de Cohere
                prompt_dinamico = f"Dame 3 ideas de títulos atractivos para un reel sobre {tema_usuario}."
                
                # Llamada a la API de Cohere
                response = client.chat(
                    message=prompt_dinamico,
                    model="command-r-plus-08-2024"
                )

                st.subheader("--- Respuesta de Cohere ---")
                st.write(response.text)
                st.success("¡Contenido generado con éxito!")
                
            except Exception as e:
                st.error(f"Ocurrió un error al consultar a Cohere: {e}")
