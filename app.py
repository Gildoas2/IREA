import streamlit as st
import os
import numpy as np
from openai import OpenAI
from utils import respuesta_openai
#------Inicialización del cliente OpenAI con la clave API desde las variables de entorno
client=OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)
#-----Mensaje para las IA's
mensaje="Extrae el texto que hay en esta imagen"
#MAIN---------------------------------------------------------------------------------------------------------------------------------------------------

def main():
    #Imagen input
    uploaded_file=st.file_uploader("Inserta un documento png",type=['png'])
    enviar=st.button("Enviar")
    tab1, tab2, tab3=st.tabs(["OpenAI","Gemini","Comparacion"])
    with tab1:
        st.header("Interpretación de OpenAI")
        if enviar:
            st.write(respuesta_openai(client,uploaded_file,mensaje))
    with tab2:
        st.header("Interpretación de Gemini")
    with tab3:
        if st.button("Comparamos los resultados"):
            st.write("Las diferencias son las siguientes:")
if __name__ == "__main__":
     main()
#--------------------------------------------------------------------------------------------------------------------------------------------------